from pathlib import Path

import pymysql

from config.settings import (
    BASE_DIR,
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
    DB_SSL_CA,
    validate_mysql_config,
)


class Database:
    @staticmethod
    def get_connection():
        validate_mysql_config()

        connection_args = {
            "host": DB_HOST,
            "port": DB_PORT,
            "user": DB_USER,
            "password": DB_PASSWORD,
            "database": DB_NAME,
            "charset": "utf8mb4",
            "cursorclass": pymysql.cursors.DictCursor,
            "connect_timeout": 10,
            "read_timeout": 10,
            "write_timeout": 10,
            "autocommit": False,
        }

        # Nếu có CA certificate thì bật xác minh SSL bằng file đó.
        if DB_SSL_CA:
            ca_path = Path(DB_SSL_CA)
            if not ca_path.is_absolute():
                ca_path = BASE_DIR / ca_path

            if not ca_path.exists():
                raise FileNotFoundError(
                    f"Không tìm thấy CA certificate: {ca_path}"
                )

            connection_args["ssl"] = {
                "ca": str(ca_path),
                "check_hostname": True,
            }

        return pymysql.connect(**connection_args)

    @staticmethod
    def initialize_database():
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS SinhVien (
                        MaSo VARCHAR(20) PRIMARY KEY,
                        HoTen VARCHAR(100) NOT NULL,
                        DiaChi VARCHAR(200)
                    )
                """)

            connection.commit()

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()
