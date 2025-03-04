#hàm kiểm tra số nhị phân có chia hết cho 5 hay không
def chia_het_cho5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#Nhập số nhị phân từ người dùng
Chuoi_so_nhi_phan = input("Nhập số nhị phân: ")
#Tách chuỗi thành các số nhị phân và kiểm tra chia hết cho 5
so_nhi_phan_list = Chuoi_so_nhi_phan.split(',')
so_chia_het_cho5 = [so for so in so_nhi_phan_list if chia_het_cho5(so)]
#in ra các số nhị phân chia hết cho 5
if len(so_chia_het_cho5) > 0:
    ket_qua = ','.join(so_chia_het_cho5)
    print("Các số nhị phân chia hết cho 5: ", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5")