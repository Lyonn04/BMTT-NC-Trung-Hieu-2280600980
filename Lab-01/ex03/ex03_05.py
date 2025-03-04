def count_elements(lst):
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

input_string = input("Enter elements of the list separated by commas: ")
word_list = input_string.split(',')
result = count_elements(word_list)
print(result)