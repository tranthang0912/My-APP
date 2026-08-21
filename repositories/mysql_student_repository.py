from database.mysql_connection import Database
from models.student import Student
from repositories.student_repository import StudentRepository


class MySQLStudentRepository(StudentRepository):
    def find_all(self):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT MaSo, HoTen, DiaChi
                    FROM SinhVien
                    ORDER BY MaSo
                """)
                rows = cursor.fetchall()

            return [
                Student(
                    ma_so=row["MaSo"],
                    ho_ten=row["HoTen"],
                    dia_chi=row["DiaChi"] or ""
                )
                for row in rows
            ]

        finally:
            connection.close()

    def find_by_id(self, ma_so):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT MaSo, HoTen, DiaChi
                    FROM SinhVien
                    WHERE MaSo = %s
                """, (ma_so,))
                row = cursor.fetchone()

            if row is None:
                return None

            return Student(
                ma_so=row["MaSo"],
                ho_ten=row["HoTen"],
                dia_chi=row["DiaChi"] or ""
            )

        finally:
            connection.close()

    def search(self, keyword):
        connection = Database.get_connection()

        try:
            pattern = f"%{keyword}%"

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT MaSo, HoTen, DiaChi
                    FROM SinhVien
                    WHERE MaSo LIKE %s
                       OR HoTen LIKE %s
                       OR DiaChi LIKE %s
                    ORDER BY MaSo
                """, (
                    pattern,
                    pattern,
                    pattern
                ))
                rows = cursor.fetchall()

            return [
                Student(
                    ma_so=row["MaSo"],
                    ho_ten=row["HoTen"],
                    dia_chi=row["DiaChi"] or ""
                )
                for row in rows
            ]

        finally:
            connection.close()

    def insert(self, student):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO SinhVien (MaSo, HoTen, DiaChi)
                    VALUES (%s, %s, %s)
                """, (
                    student.ma_so,
                    student.ho_ten,
                    student.dia_chi
                ))

            connection.commit()
            return True

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()

    def update(self, old_ma_so, student):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE SinhVien
                    SET MaSo = %s,
                        HoTen = %s,
                        DiaChi = %s
                    WHERE MaSo = %s
                """, (
                    student.ma_so,
                    student.ho_ten,
                    student.dia_chi,
                    old_ma_so
                ))

                success = cursor.rowcount > 0

            connection.commit()
            return success

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()

    def delete(self, ma_so):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM SinhVien
                    WHERE MaSo = %s
                """, (ma_so,))

                success = cursor.rowcount > 0

            connection.commit()
            return success

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()
