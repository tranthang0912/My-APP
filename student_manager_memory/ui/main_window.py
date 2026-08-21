import tkinter as tk
from tkinter import ttk


class MainWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Quản lý sinh viên")
        self.root.geometry("900x600")

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="QUẢN LÝ SINH VIÊN",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=20)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Mã số:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.ma_so = tk.Entry(frame, width=30)
        self.ma_so.grid(row=0, column=1)

        tk.Label(
            frame,
            text="Họ tên:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.ho_ten = tk.Entry(frame, width=30)
        self.ho_ten.grid(row=1, column=1)

        tk.Label(
            frame,
            text="Địa chỉ:"
        ).grid(row=2, column=0, padx=10, pady=10)

        self.dia_chi = tk.Entry(frame, width=30)
        self.dia_chi.grid(row=2, column=1)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="THÊM",
            width=12
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="SỬA",
            width=12
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="XÓA",
            width=12
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="LÀM MỚI",
            width=12
        ).grid(row=0, column=3, padx=5)

        columns = (
            "MaSo",
            "HoTen",
            "DiaChi"
        )

        self.table = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings"
        )

        self.table.heading("MaSo", text="Mã số")
        self.table.heading("HoTen", text="Họ tên")
        self.table.heading("DiaChi", text="Địa chỉ")

        self.table.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )