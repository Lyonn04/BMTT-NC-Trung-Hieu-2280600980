def tinh_TongSoChan(lst):
    tong =0
    for i in lst:
        if i%2 == 0:
            tong += i
    return tong
#Nhập các dòng từ người dùng
input_list  = input("nhập danh sách các số ")
number = list(map(int,input_list.split()))
tong_chan = tinh_TongSoChan(number)
print("Tổng các số chẳn trong danh sách là: ", tong_chan)