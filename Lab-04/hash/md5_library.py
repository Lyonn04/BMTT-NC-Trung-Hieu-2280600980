import hashlib 
def callable_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Nhap chuoi can bam: ")
md5_hash = callable_md5(input_string)

print("Ma hoa MD5 cua chuoi '{}' la: {}".format(input_string, md5_hash))
