from abc import ABC, abstractmethod


class StudentRepository(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, ma_so):
        pass

    @abstractmethod
    def search(self, keyword):
        pass

    @abstractmethod
    def insert(self, student):
        pass

    @abstractmethod
    def update(self, old_ma_so, student):
        pass

    @abstractmethod
    def delete(self, ma_so):
        pass
