import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.mysql_connection import Database


def main():
    connection = Database.get_connection()

    try:
        with connection.cursor() as cursor:

            print("\n===== DATABASE HIỆN TẠI =====")
            cursor.execute("SELECT DATABASE() AS db")
            print(cursor.fetchone()["db"])

            print("\n===== DANH SÁCH DATABASE =====")
            cursor.execute("SHOW DATABASES")

            for row in cursor.fetchall():
                print(row)

            print("\n===== DANH SÁCH TABLE =====")
            cursor.execute("SHOW TABLES")

            tables = cursor.fetchall()

            for table in tables:
                print(table)

            print("\n===== CẤU TRÚC BẢNG SinhVien =====")
            cursor.execute("DESCRIBE SinhVien")

            for row in cursor.fetchall():
                print(row)

            print("\n===== DỮ LIỆU BẢNG SinhVien =====")
            cursor.execute("""
                SELECT MaSo, HoTen, DiaChi
                FROM SinhVien
                ORDER BY MaSo
            """)

            rows = cursor.fetchall()

            if not rows:
                print("Bảng chưa có dữ liệu.")
            else:
                for row in rows:
                    print(
                        row["MaSo"],
                        "|",
                        row["HoTen"],
                        "|",
                        row["DiaChi"]
                    )

    finally:
        connection.close()


if __name__ == "__main__":
    main()