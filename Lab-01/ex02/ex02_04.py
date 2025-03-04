#Tạo 1 danh sách rỗng để lưu kết quả 
a =[]
#Duyệt qua tất cả các số từ 2000 đến 3200, kiểm tra xem số i có chia hết cho 7 va không là bội số của 5 hay không
for i in range (2000, 3201):
    if(i % 7 == 0) and (i % 5 != 0):
        a.append(str(i))
    print (','.join(a))
        