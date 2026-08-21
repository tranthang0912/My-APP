import tkinter as tk

from repositories.memory_student_repository import MemoryStudentRepository
from services.student_service import StudentService
from ui.main_window import MainWindow


def main():
    repository = MemoryStudentRepository()
    service = StudentService(repository)

    root = tk.Tk()
    MainWindow(root, service)
    root.mainloop()


if __name__ == "__main__":
    main()
