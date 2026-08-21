from repositories.sinhvien_repository import SinhVienRepository


class SinhVienService:

    def __init__(self):
        self.repository = SinhVienRepository()

    def get_all(self):
        return self.repository.get_all()

    def add(self, sinh_vien):
        self.repository.add(sinh_vien)

    def update(self, sinh_vien):
        self.repository.update(sinh_vien)

    def delete(self, ma_so):
        self.repository.delete(ma_so)   