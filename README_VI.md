# Công Cụ Tính Tiền Điện Nước Nhà Cho Thuê

```text
Công Cụ Tính Tiền Điện Nước Nhà Cho Thuê
│
├── Tổng Quan Dự Án
│   ├── Công cụ Python tính chi phí thuê nhà
│   ├── Chạy bằng giao diện dòng lệnh (CLI)
│   └── Hỗ trợ tính tổng chi phí hàng tháng
│
├── Chức Năng Chính
│   │
│   ├── Tính Tiền Điện
│   │   ├── Tính số điện tiêu thụ (kWh)
│   │   ├── So sánh chỉ số điện mới/cũ
│   │   └── Tính tổng tiền điện
│   │
│   ├── Tính Tiền Nước
│   │   ├── Tính số nước tiêu thụ (m3)
│   │   ├── So sánh chỉ số nước mới/cũ
│   │   └── Tính tổng tiền nước
│   │
│   ├── Tiền Thuê Nhà
│   │   └── Thêm chi phí thuê cố định
│   │
│   └── Tổng Thanh Toán
│       ├── Tổng hợp toàn bộ chi phí
│       └── Hiển thị số tiền cuối cùng
│
├── Luồng Nhập Dữ Liệu
│   │
│   ├── Điện
│   │   ├── Chỉ số điện mới
│   │   └── Chỉ số điện cũ
│   │
│   └── Nước
│       ├── Chỉ số nước mới
│       └── Chỉ số nước cũ
│
├── Luồng Tính Toán
│   │
│   ├── Điện Tiêu Thụ
│   │   └── chỉ_số_mới - chỉ_số_cũ
│   │
│   ├── Nước Tiêu Thụ
│   │   └── chỉ_số_mới - chỉ_số_cũ
│   │
│   ├── Chi Phí Tiện Ích
│   │   ├── điện_tiêu_thụ × giá_điện
│   │   └── nước_tiêu_thụ × giá_nước
│   │
│   └── Tổng Hóa Đơn
│       └── tiền_nhà + tiền_điện + tiền_nước
│
├── Cấu Hình Giá
│   │
│   ├── Tiền Thuê Nhà
│   │   └── 1,200,000 VND
│   │
│   ├── Giá Điện
│   │   └── 4,000 VND / kWh
│   │
│   └── Giá Nước
│       └── 10,000 VND / m3
│
├── Cấu Trúc Project
│
│   project/
│   ├── english_version.py
│   ├── vietnamese_version.py
│   └── README.md
│
├── Cách Chạy Chương Trình
│   │
│   ├── Lệnh Chạy
│   │
│   │   python vietnamese_version.py
│   │
│   └── Loại Giao Diện
│       └── Command-line interface (CLI)
│
├── Ví Dụ Hoạt Động
│   │
│   ├── Nhập Điện
│   │   ├── Chỉ số mới: 120
│   │   └── Chỉ số cũ: 100
│   │
│   ├── Nhập Nước
│   │   ├── Chỉ số mới: 15
│   │   └── Chỉ số cũ: 10
│   │
│   ├── Kết Quả Tiêu Thụ
│   │   ├── Điện: 20 kWh
│   │   └── Nước: 5 m3
│   │
│   └── Tổng Chi Phí
│       ├── Tiền điện: 80,000 VND
│       ├── Tiền nước: 50,000 VND
│       ├── Tiền nhà: 1,200,000 VND
│       └── Tổng tất cả: 1,330,000 VND
│
└── Mục Đích Dự Án
    │
    ├── Luyện tập hàm trong Python
    ├── Sử dụng biến và hằng số
    ├── Nhập dữ liệu từ người dùng
    ├── Thực hành phép tính cơ bản
    ├── Tổ chức cấu trúc code
    └── Làm quen chương trình CLI
```
