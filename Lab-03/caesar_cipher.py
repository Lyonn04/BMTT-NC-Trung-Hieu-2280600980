import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests
import os 
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        try:
            key = int(self.ui.textEdit_3.toPlainText())
        except ValueError:
            QMessageBox.critical(self, "Lỗi", "Key phải là một số nguyên")
            return

        payload = {
            "plain_text": self.ui.textEdit.toPlainText(),
            "key": key
        }

        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_2.setPlainText(data["encrypted_text"])
                QMessageBox.information(self, "Thông báo", "Mã hóa thành công!")
            else:
                QMessageBox.critical(self, "Lỗi", f"Lỗi từ API: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        try:
            key = int(self.ui.textEdit_3.toPlainText())
        except ValueError:
            QMessageBox.critical(self, "Lỗi", "Key phải là một số nguyên")
            return

        payload = {
            "cipher_text": self.ui.textEdit_2.toPlainText(),
            "key": key
        }

        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setPlainText(data["decrypted_text"])
                QMessageBox.information(self, "Thông báo", "Giải mã thành công!")
            else:
                QMessageBox.critical(self, "Lỗi", f"Lỗi từ API: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())