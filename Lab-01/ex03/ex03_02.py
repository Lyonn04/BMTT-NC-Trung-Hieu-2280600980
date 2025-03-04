def reverse_list(input_list):
    return input_list[::-1]

# Example usage
if __name__ == "__main__":
    sample_list = input("Enter a list of numbers separated by spaces: ").split()
    sample_list = [int(x) for x in sample_list]
    reversed_list = reverse_list(sample_list)
    print("Original list:", sample_list)
    print("Reversed list:", reversed_list)