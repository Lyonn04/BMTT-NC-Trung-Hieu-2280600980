def test(n):
    if(n<=1):
        return False
    for i in range(2,int(n** 0.5)+1):
        if(n%i==0):
            return False
    return True
#kiểm tra số nguyên tố va in kết quả 
number = int(input("Nhập số cần kiểm tra:  "))
if( test(number)):
    print("Đây là số nguyên tố")
else:
    print(number, "không phải số nguyên tố")