#Nhập các dòng từ người dùng
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
#chuyển các dòng văn bản thành chữ in hoa
print("\ncác dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())
        