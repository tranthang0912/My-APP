# Student Manager - Python Tkinter + MySQL Cloud

Ứng dụng quản lý sinh viên với giao diện Tkinter và MySQL.

## Chức năng

- SELECT: hiển thị toàn bộ danh sách
- SELECT WHERE / LIKE: tìm kiếm
- INSERT: thêm sinh viên
- UPDATE: sửa sinh viên
- DELETE: xóa sinh viên
- Click một dòng để đưa dữ liệu lên form
- Kiểm tra mã sinh viên trùng
- Xác nhận trước khi xóa

## Cấu trúc

```text
student_manager_mysql_cloud/
├── main.py
├── requirements.txt
├── .gitignore
├── .env.example
├── config/
├── database/
├── models/
├── repositories/
├── services/
├── ui/
├── scripts/
└── sql/
```

## 1. Cài thư viện

```bash
pip install -r requirements.txt
```

## 2. Tạo file .env

Copy `.env.example` thành `.env`.

Windows CMD:

```bat
copy .env.example .env
```

PowerShell:

```powershell
Copy-Item .env.example .env
```

Hoặc tạo/copy bằng giao diện VS Code.

## 3. Điền thông tin MySQL

Ví dụ Aiven cấp:

- Host: `mysql-abc-project.aivencloud.com`
- Port: `18765`
- User: `avnadmin`
- Password: `AbcXYZ123!`
- Database: `defaultdb`

thì `.env`:

```env
APP_STORAGE=mysql
DB_HOST=mysql-abc-project.aivencloud.com
DB_PORT=18765
DB_USER=avnadmin
DB_PASSWORD=AbcXYZ123!
DB_NAME=defaultdb
DB_SSL_CA=
```

Nếu đã tạo database `QuanLySinhVien`, đổi:

```env
DB_NAME=QuanLySinhVien
```

## 4. Test kết nối

```bash
python scripts/test_connection.py
```

Nếu thành công sẽ hiện thông tin MySQL và database đang dùng.

## 5. Chạy ứng dụng

```bash
python main.py
```

Chương trình tự tạo bảng:

```sql
SinhVien(
    MaSo PRIMARY KEY,
    HoTen,
    DiaChi
)
```

nếu bảng chưa tồn tại.

## Chạy thử không cần database

Trong `.env`:

```env
APP_STORAGE=memory
```

Dữ liệu lúc này chỉ nằm trong RAM và mất khi đóng app.

## GitHub

`.env` đã nằm trong `.gitignore`, do đó không push password.

Trước khi push luôn kiểm tra:

```bash
git status
```

Nếu thấy `.env`, KHÔNG push.
