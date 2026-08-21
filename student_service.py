from models.student import Student


class StudentService:
    def __init__(self, repository):
        self.repository = repository

    @staticmethod
    def _clean_data(ma_so, ho_ten, dia_chi):
        return (
            ma_so.strip(),
            ho_ten.strip(),
            dia_chi.strip()
        )

    def get_all_students(self):
        return self.repository.find_all()

    def search_students(self, keyword):
        keyword = keyword.strip()

        if not keyword:
            return self.get_all_students()

        return self.repository.search(keyword)

    def add_student(self, ma_so, ho_ten, dia_chi):
        ma_so, ho_ten, dia_chi = self._clean_data(
            ma_so,
            ho_ten,
            dia_chi
        )

        if not ma_so:
            raise ValueError("Mã số không được để trống.")

        if not ho_ten:
            raise ValueError("Họ tên không được để trống.")

        if self.repository.find_by_id(ma_so):
            raise ValueError("Mã sinh viên đã tồn tại.")

        student = Student(
            ma_so=ma_so,
            ho_ten=ho_ten,
            dia_chi=dia_chi
        )

        self.repository.insert(student)

    def update_student(
        self,
        old_ma_so,
        ma_so,
        ho_ten,
        dia_chi
    ):
        if not old_ma_so:
            raise ValueError("Hãy chọn sinh viên cần sửa.")

        ma_so, ho_ten, dia_chi = self._clean_data(
            ma_so,
            ho_ten,
            dia_chi
        )

        if not ma_so:
            raise ValueError("Mã số không được để trống.")

        if not ho_ten:
            raise ValueError("Họ tên không được để trống.")

        if ma_so != old_ma_so:
            duplicated_student = self.repository.find_by_id(ma_so)

            if duplicated_student:
                raise ValueError("Mã sinh viên mới đã tồn tại.")

        student = Student(
            ma_so=ma_so,
            ho_ten=ho_ten,
            dia_chi=dia_chi
        )

        success = self.repository.update(
            old_ma_so,
            student
        )

        if not success:
            raise ValueError("Không tìm thấy sinh viên cần sửa.")

    def delete_student(self, ma_so):
        if not ma_so:
            raise ValueError("Hãy chọn sinh viên cần xóa.")

        success = self.repository.delete(ma_so)

        if not success:
            raise ValueError("Không tìm thấy sinh viên cần xóa.")
