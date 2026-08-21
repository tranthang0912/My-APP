from repositories.student_repository import StudentRepository


class MemoryStudentRepository(StudentRepository):
    def __init__(self):
        self.students = {}

    def find_all(self):
        return sorted(
            self.students.values(),
            key=lambda student: student.ma_so.lower()
        )

    def find_by_id(self, ma_so):
        return self.students.get(ma_so)

    def search(self, keyword):
        keyword = keyword.strip().lower()

        result = []

        for student in self.students.values():
            if (
                keyword in student.ma_so.lower()
                or keyword in student.ho_ten.lower()
                or keyword in student.dia_chi.lower()
            ):
                result.append(student)

        return sorted(
            result,
            key=lambda student: student.ma_so.lower()
        )

    def insert(self, student):
        self.students[student.ma_so] = student
        return True

    def update(self, old_ma_so, student):
        if old_ma_so not in self.students:
            return False

        del self.students[old_ma_so]
        self.students[student.ma_so] = student
        return True

    def delete(self, ma_so):
        if ma_so not in self.students:
            return False

        del self.students[ma_so]
        return True
