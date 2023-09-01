# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Prints 1
print(my_list[-1])  # Prints 5

# Modifying elements
my_list[2] = 10
print(my_list)  # Prints [1, 2, 10, 4, 5]

# Appending elements
my_list.append(6)
print(my_list)  # Prints [1, 2, 10, 4, 5, 6]

# Removing elements
my_list.remove(4)
print(my_list)  # Prints [1, 2, 10, 5, 6]

# List comprehension
squares = [x**2 for x in my_list]
print(squares)  # Prints [1, 4, 100, 25, 36]
