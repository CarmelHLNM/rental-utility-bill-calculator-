# CÔNG CỤ TÍNH TIỀN ĐIỆN NƯỚC NHÀ CHO THUÊ

TIEN_THUE = 1_200_000
GIA_DIEN = 4000
GIA_NUOC = 10000


def tinh_tien_dien(chi_so_moi, chi_so_cu):
    dien_tieu_thu = chi_so_moi - chi_so_cu
    tien_dien = dien_tieu_thu * GIA_DIEN

    print(f"Điện tiêu thụ: {dien_tieu_thu} kWh")
    print("\n" * 3)
    print("〰️" * 8)

    return tien_dien


def tinh_tien_nuoc(chi_so_moi, chi_so_cu):
    nuoc_tieu_thu = chi_so_moi - chi_so_cu
    tien_nuoc = nuoc_tieu_thu * GIA_NUOC

    print(f"Nước tiêu thụ: {nuoc_tieu_thu} m3")
    print("\n" * 3)
    print("〰️" * 8)

    return tien_nuoc


def tinh_tong_hoa_don(tien_dien, tien_nuoc):
    tong_tien = tien_dien + tien_nuoc + TIEN_THUE

    print(f"Tổng tiền điện: {tien_dien:,} VND")
    print(f"Tổng tiền nước: {tien_nuoc:,} VND")
    print(f"Tiền thuê nhà: {TIEN_THUE:,} VND")
    print(f"Tổng phải trả: {tong_tien:,} VND")


tinh_tong_hoa_don(
    tien_dien=tinh_tien_dien(
        chi_so_moi=int(input("Nhập chỉ số điện mới: ")),
        chi_so_cu=int(input("Nhập chỉ số điện cũ: "))
    ),

    tien_nuoc=tinh_tien_nuoc(
        chi_so_moi=int(input("Nhập chỉ số nước mới: ")),
        chi_so_cu=int(input("Nhập chỉ số nước cũ: "))
    )
)
