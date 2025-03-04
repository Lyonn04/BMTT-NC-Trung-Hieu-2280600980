# Chương trình để tạo một tuple từ một list nhập vào từ bàn phím
def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhập list từ bàn phím, các phần tử cách nhau bởi dấu phẩy
input_list = input("Nhập các phần tử của list, cách nhau bởi dấu phẩy: ").split(',')


# Chuyển đổi list thành tuple
output_tuple = tuple(input_list)

# In ra tuple
print("Tuple được tạo từ list đã nhập:", output_tuple)