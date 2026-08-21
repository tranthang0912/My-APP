import sys
from pathlib import Path

# Cho phép chạy trực tiếp: python scripts/test_connection.py
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.mysql_connection import Database


def main():
    connection = None

    try:
        connection = Database.get_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    VERSION() AS version,
                    DATABASE() AS database_name,
                    CURRENT_USER() AS current_user_name
            """)
            result = cursor.fetchone()

        print("=" * 50)
        print("KẾT NỐI MYSQL THÀNH CÔNG")
        print("MySQL version :", result["version"])
        print("Database      :", result["database_name"])
        print("Current user  :", result["current_user_name"])
        print("=" * 50)

    except Exception as error:
        print("=" * 50)
        print("KẾT NỐI MYSQL THẤT BẠI")
        print(error)
        print("=" * 50)

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    main()
