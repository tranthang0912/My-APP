# Student Manager

Ứng dụng quản lý sinh viên bằng Python Tkinter.

## Chức năng

- Hiển thị danh sách sinh viên
- Thêm sinh viên
- Sửa sinh viên
- Xóa sinh viên
- Tìm kiếm theo mã số, họ tên hoặc địa chỉ
- Click vào một dòng để đưa dữ liệu lên form
- Kiểm tra dữ liệu đầu vào
- Xác nhận trước khi xóa

## Công nghệ

- Python 3
- Tkinter
- Repository Pattern
- Service Layer

## Lưu ý

Phiên bản hiện tại dùng `MemoryStudentRepository`, vì vậy dữ liệu chỉ tồn tại khi chương trình đang chạy.

Khi tích hợp MySQL sau này, chỉ cần bổ sung `MySQLStudentRepository` và đổi repository trong `main.py`.

## Cấu trúc

```text
student_manager_memory/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── models/
├── repositories/
├── services/
└── ui/
```

## Chạy chương trình

```bash
python main.py
```

Trên Windows cũng có thể dùng:

```bash
py main.py
```

## GitHub

Khởi tạo Git:

```bash
git init
git add .
git commit -m "feat: initialize student manager"
git branch -M main
```

Sau đó kết nối repository GitHub:

```bash
git remote add origin <URL_REPOSITORY_CUA_BAN>
git push -u origin main
```
