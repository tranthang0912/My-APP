import tkinter as tk
from tkinter import ttk, messagebox


class MainWindow:
    def __init__(self, root, service):
        self.root = root
        self.service = service
        self.selected_ma_so = None

        self.ma_so_var = tk.StringVar()
        self.ho_ten_var = tk.StringVar()
        self.dia_chi_var = tk.StringVar()
        self.search_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Sẵn sàng")

        self._setup_window()
        self._build_title()
        self._build_form()
        self._build_buttons()
        self._build_search()
        self._build_table()
        self._build_status_bar()

        self.load_students()

    def _setup_window(self):
        self.root.title("Quản lý sinh viên")
        self.root.geometry("920x620")
        self.root.minsize(820, 560)

    def _build_title(self):
        title = ttk.Label(
            self.root,
            text="QUẢN LÝ SINH VIÊN",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=(15, 8))

        subtitle = ttk.Label(
            self.root,
            text="SELECT - INSERT - UPDATE - DELETE",
            font=("Segoe UI", 10)
        )
        subtitle.pack(pady=(0, 8))

    def _build_form(self):
        frame = ttk.LabelFrame(
            self.root,
            text="Thông tin sinh viên",
            padding=12
        )
        frame.pack(fill="x", padx=15, pady=5)

        ttk.Label(frame, text="Mã số:").grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=7
        )

        self.ma_so_entry = ttk.Entry(
            frame,
            textvariable=self.ma_so_var
        )
        self.ma_so_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=7
        )

        ttk.Label(frame, text="Họ tên:").grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=7
        )

        ttk.Entry(
            frame,
            textvariable=self.ho_ten_var
        ).grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=7
        )

        ttk.Label(frame, text="Địa chỉ:").grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=7
        )

        ttk.Entry(
            frame,
            textvariable=self.dia_chi_var
        ).grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=7
        )

        frame.columnconfigure(1, weight=1)

    def _build_buttons(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="x", padx=15, pady=8)

        ttk.Button(
            frame,
            text="Thêm",
            command=self.add_student
        ).pack(side="left", padx=4)

        ttk.Button(
            frame,
            text="Sửa",
            command=self.update_student
        ).pack(side="left", padx=4)

        ttk.Button(
            frame,
            text="Xóa",
            command=self.delete_student
        ).pack(side="left", padx=4)

        ttk.Button(
            frame,
            text="Làm mới",
            command=self.clear_form
        ).pack(side="left", padx=4)

    def _build_search(self):
        frame = ttk.LabelFrame(
            self.root,
            text="Tìm kiếm",
            padding=10
        )
        frame.pack(fill="x", padx=15, pady=5)

        ttk.Label(
            frame,
            text="Mã số / Họ tên / Địa chỉ:"
        ).pack(side="left", padx=(0, 8))

        search_entry = ttk.Entry(
            frame,
            textvariable=self.search_var
        )
        search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=4
        )

        search_entry.bind(
            "<Return>",
            lambda event: self.search_students()
        )

        ttk.Button(
            frame,
            text="Tìm kiếm",
            command=self.search_students
        ).pack(side="left", padx=4)

        ttk.Button(
            frame,
            text="Hiển thị tất cả",
            command=self.show_all
        ).pack(side="left", padx=4)

    def _build_table(self):
        frame = ttk.Frame(self.root)
        frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(5, 10)
        )

        columns = (
            "MaSo",
            "HoTen",
            "DiaChi"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        self.tree.heading("MaSo", text="Mã số")
        self.tree.heading("HoTen", text="Họ tên")
        self.tree.heading("DiaChi", text="Địa chỉ")

        self.tree.column(
            "MaSo",
            width=150,
            anchor="center"
        )
        self.tree.column(
            "HoTen",
            width=280
        )
        self.tree.column(
            "DiaChi",
            width=350
        )

        scroll_y = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=self.tree.yview
        )

        scroll_x = ttk.Scrollbar(
            frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        scroll_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )
        scroll_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_tree_select
        )

    def _build_status_bar(self):
        ttk.Label(
            self.root,
            textvariable=self.status_var,
            anchor="w",
            relief="sunken"
        ).pack(
            fill="x",
            side="bottom"
        )

    def load_students(self, students=None):
        if students is None:
            students = self.service.get_all_students()

        self._show_students(students)

    def _show_students(self, students):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for student in students:
            self.tree.insert(
                "",
                "end",
                values=(
                    student.ma_so,
                    student.ho_ten,
                    student.dia_chi
                )
            )

        self.status_var.set(
            f"Đang hiển thị {len(students)} sinh viên."
        )

    def add_student(self):
        try:
            self.service.add_student(
                self.ma_so_var.get(),
                self.ho_ten_var.get(),
                self.dia_chi_var.get()
            )

            messagebox.showinfo(
                "Thành công",
                "Thêm sinh viên thành công."
            )

            self.clear_form()
            self.load_students()

        except ValueError as error:
            messagebox.showwarning(
                "Thông báo",
                str(error)
            )

    def update_student(self):
        try:
            self.service.update_student(
                self.selected_ma_so,
                self.ma_so_var.get(),
                self.ho_ten_var.get(),
                self.dia_chi_var.get()
            )

            messagebox.showinfo(
                "Thành công",
                "Cập nhật sinh viên thành công."
            )

            self.clear_form()
            self.load_students()

        except ValueError as error:
            messagebox.showwarning(
                "Thông báo",
                str(error)
            )

    def delete_student(self):
        if not self.selected_ma_so:
            messagebox.showwarning(
                "Thông báo",
                "Hãy chọn sinh viên cần xóa."
            )
            return

        confirm = messagebox.askyesno(
            "Xác nhận xóa",
            f"Bạn có chắc muốn xóa sinh viên '{self.selected_ma_so}' không?"
        )

        if not confirm:
            return

        try:
            self.service.delete_student(
                self.selected_ma_so
            )

            messagebox.showinfo(
                "Thành công",
                "Xóa sinh viên thành công."
            )

            self.clear_form()
            self.load_students()

        except ValueError as error:
            messagebox.showwarning(
                "Thông báo",
                str(error)
            )

    def search_students(self):
        students = self.service.search_students(
            self.search_var.get()
        )

        self._show_students(students)

    def show_all(self):
        self.search_var.set("")
        self.load_students()

    def on_tree_select(self, event=None):
        selected = self.tree.selection()

        if not selected:
            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        if len(values) < 3:
            return

        self.selected_ma_so = values[0]
        self.ma_so_var.set(values[0])
        self.ho_ten_var.set(values[1])
        self.dia_chi_var.set(values[2])

    def clear_form(self):
        self.selected_ma_so = None

        self.ma_so_var.set("")
        self.ho_ten_var.set("")
        self.dia_chi_var.set("")

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.ma_so_entry.focus()
