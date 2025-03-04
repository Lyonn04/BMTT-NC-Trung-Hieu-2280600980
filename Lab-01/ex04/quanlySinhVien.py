from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxID = 1
        if self.SoLuongSV() > 0:
            maxID = max(sv._id for sv in self.listSinhVien) + 1
        return maxID
    
    def SoLuongSV(self):
        return len(self.listSinhVien)
    
    def nhapSV(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap nganh hoc: ")
        avg_score = float(input("Nhap diem trung binh: "))
        sv = SinhVien(svID, name, sex, major, avg_score)
        self.xephangHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            sv._name = input("Nhap ten sinh vien: ")
            sv._sex = input("Nhap gioi tinh: ")
            sv._major = input("Nhap nganh hoc: ")
            sv._avg_score = float(input("Nhap diem trung binh: "))
            self.xephangHocLuc(sv)
        else:
            print("Khong tim thay sinh vien")
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def sortByAvg_Score(self):
        self.listSinhVien.sort(key=lambda x: x._avg_score)

    def sortByMajor(self):
        self.listSinhVien.sort(key=lambda x: x._major)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        listSv = [sv for sv in self.listSinhVien if keyword.upper() in sv._name.upper()]
        self.showSinhVien(listSv)
        return listSv

    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xephangHocLuc(self, sv):
        if sv._avg_score >= 8.0:
            sv._hocluc = "Gioi"
        elif sv._avg_score >= 7.0:
            sv._hocluc = "Kha"
        elif sv._avg_score >= 5.0:
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"

    def showSinhVien(self, listsv):
        print("{:<8} {:<18} {:<8} {:<12} {:<10} {:<10}".format("ID", "Name", "Sex", "Major", "Avg_Score", "Hoc Luc"))
        for sv in listsv:
            print("{:<8} {:<18} {:<8} {:<12} {:<10} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._avg_score, sv._hocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
