CREATE DATABASE QLSinhVien;
GO

USE QLSinhVien;
GO

CREATE TABLE SinhVien
(
    MaSo VARCHAR(20) PRIMARY KEY,
    HoTen NVARCHAR(100) NOT NULL,
    DiaChi NVARCHAR(200)
);
GO

INSERT INTO SinhVien (MaSo, HoTen, DiaChi)
VALUES
('SV001', N'Nguyễn Văn An', N'TP.HCM'),
('SV002', N'Trần Văn Bình', N'Đồng Nai'),
('SV003', N'Lê Văn Cường', N'Bình Dương');
GO