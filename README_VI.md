# Công Cụ Tính Tiền Điện Nước Nhà Cho Thuê

Một công cụ Python đơn giản dùng để tính chi phí thuê nhà bao gồm:

- Tiền điện
- Tiền nước
- Tiền thuê nhà
- Tổng chi phí cần thanh toán

## Tính Năng

- Tính số điện tiêu thụ (kWh)
- Tính số nước tiêu thụ (m3)
- Tự động tính tổng hóa đơn hàng tháng
- Giao diện dòng lệnh đơn giản

## Cấu Trúc Project

```text
project/
├── english_version.py
├── vietnamese_version.py
└── README.md
```

## Cách Hoạt Động

Người dùng nhập:

- Chỉ số điện mới
- Chỉ số điện cũ
- Chỉ số nước mới
- Chỉ số nước cũ

Chương trình sẽ tự động tính:

- Tiền điện
- Tiền nước
- Tiền thuê nhà
- Tổng số tiền cần thanh toán

## Cấu Hình Giá

Mức giá hiện tại:

- Tiền thuê nhà: 1,200,000 VND
- Giá điện: 4,000 VND / kWh
- Giá nước: 10,000 VND / m3

Bạn có thể chỉnh sửa các giá trị này trực tiếp trong code.

## Cách Chạy Chương Trình

Chạy file Python:

```bash
python vietnamese_version.py
```

## Ví Dụ

```text
Nhập chỉ số điện mới: 120
Nhập chỉ số điện cũ: 100

Số điện tiêu thụ: 20 kWh

Nhập chỉ số nước mới: 15
Nhập chỉ số nước cũ: 10

Số nước tiêu thụ: 5 m3

Tổng tiền điện: 80,000 VND
Tổng tiền nước: 50,000 VND
Tiền thuê nhà: 1,200,000 VND

Tổng tất cả: 1,330,000 VND
```

## Mục Đích Dự Án

Project này được tạo để luyện tập:

- Hàm trong Python
- Biến và hằng số
- Nhập dữ liệu từ người dùng
- Các phép tính cơ bản
- Tổ chức code
