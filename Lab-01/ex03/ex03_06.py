def remove_key_from_dict(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False


# Example usage
sample_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
result = remove_key_from_dict(sample_dict, key_to_remove)
if result:
    print("phần tử đã được xoá từ dictionary",sample_dict)
else:
    print("phần tử không tồn tại trong dictionary")