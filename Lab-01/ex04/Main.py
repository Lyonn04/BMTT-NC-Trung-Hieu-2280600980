from quanlySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("**********************************MENU**********************************")
    print("1. Nhap sinh vien")
    print("2. Cap nhat thong tin sinh vien")
    print("3. Xoa sinh vien")  
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    print("************************************************************************")
    key = int(input("Nhap lua chon cua ban: "))
    if(key==1):
        print("\n1. Them sinh vien")
        qlsv.nhapSV()
        print("\nthem sinh vien thanh cong!")
    elif(key==2):
        if(qlsv.SoLuongSV()>0):
            print("\n2. Cap nhat thong tin sinh vien")
            ID = int(input("Nhap ID cua sinh vien can cap nhat: "))
            qlsv.updateSinhVien(ID)
            print("\nCap nhat sinh vien thanh cong!")
        else:
            print("Danh sach sinh vien rong!")
    elif(key==3):
        if(qlsv.SoLuongSV()>0):
            print("\n3. Xoa sinh vien")
            ID = int(input("Nhap ID cua sinh vien can xoa: "))
            qlsv.deleteSinhVien(ID)
            print("\nXoa sinh vien thanh cong!")
        else:
            print("Danh sach sinh vien rong!")
    elif(key==4):
        if(qlsv.SoLuongSV()>0):
            print("\n4. Tim kiem sinh vien theo ten")
            name = input("Nhap ten sinh vien can tim: ")
            qlsv.findByName(name)
        else:
            print("Danh sach sinh vien rong!")
    elif(key==5):
        if(qlsv.SoLuongSV()>0):
            print("\n5. Sap xep sinh vien theo diem trung binh")
            qlsv.sortByAvg_Score()
            qlsv.showList()
        else:
            print("Danh sach sinh vien rong!")
    elif(key==6):
        if(qlsv.SoLuongSV()>0):
            print("\n6. Sap xep sinh vien theo ten chuyen nganh")
            qlsv.sortByMajor()
            qlsv.showList()
        else:
            print("Danh sach sinh vien rong!")
    elif(key==7):
        if(qlsv.SoLuongSV()>0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showList()
        else:
            print("Danh sach sinh vien rong!")
    elif(key==0):
        break
    else:
        print("Lua chon khong hop le!")
        print("\nHay chon lai!")