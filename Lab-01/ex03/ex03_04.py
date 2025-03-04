# Get user input and convert it to a tuple
user_input = input("Enter elements of the tuple separated by commas: ")
user_tuple = tuple(user_input.split(','))

# Access the first and last elements
first_element = user_tuple[0]
last_element = user_tuple[-1]

# Print the results
print(f"First element: {first_element}")
print(f"Last element: {last_element}")