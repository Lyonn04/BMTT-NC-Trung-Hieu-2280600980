input_str = input("Nhập X,Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNUM = dimensions[0]
columNUM = dimensions[1]
multilist = [[0 for col in range(columNUM)] for row in range(rowNUM)]
for row in range(rowNUM):
    for col in range(columNUM):
        multilist[row][col] = row*col
print(multilist)