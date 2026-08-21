import tkinter as tk
from tkinter import messagebox

from config.settings import APP_STORAGE
from database.mysql_connection import Database
from repositories.memory_student_repository import MemoryStudentRepository
from repositories.mysql_student_repository import MySQLStudentRepository
from services.student_service import StudentService
from ui.main_window import MainWindow


def build_repository():
    if APP_STORAGE.lower() == "memory":
        return MemoryStudentRepository()

    # Chế độ mặc định: MySQL
    Database.initialize_database()
    return MySQLStudentRepository()


def main():
    root = tk.Tk()
    root.withdraw()

    try:
        repository = build_repository()
    except Exception as error:
        messagebox.showerror(
            "Lỗi kết nối MySQL",
            "Không thể kết nối tới database.\n\n"
            f"Chi tiết: {error}\n\n"
            "Hãy kiểm tra file .env và đảm bảo Host / Port / User / Password / Database đúng."
        )
        root.destroy()
        return

    service = StudentService(repository)

    root.deiconify()
    MainWindow(root, service)
    root.mainloop()


if __name__ == "__main__":
    main()
