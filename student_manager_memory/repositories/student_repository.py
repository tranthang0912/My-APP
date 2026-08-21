from config.database import get_connection
from models.sinhvien import SinhVien


class SinhVienRepository:

    def get_all(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT MaSo, HoTen, DiaChi FROM SinhVien"
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            SinhVien(row[0], row[1], row[2])
            for row in rows
        ]

    def add(self, sinh_vien):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO SinhVien
            (MaSo, HoTen, DiaChi)
            VALUES (?, ?, ?)
            """,
            sinh_vien.ma_so,
            sinh_vien.ho_ten,
            sinh_vien.dia_chi
        )

        conn.commit()

        cursor.close()
        conn.close()

    def update(self, sinh_vien):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE SinhVien
            SET HoTen = ?,
                DiaChi = ?
            WHERE MaSo = ?
            """,
            sinh_vien.ho_ten,
            sinh_vien.dia_chi,
            sinh_vien.ma_so
        )

        conn.commit()

        cursor.close()
        conn.close()

    def delete(self, ma_so):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM SinhVien WHERE MaSo = ?",
            ma_so
        )

        conn.commit()

        cursor.close()
        conn.close()