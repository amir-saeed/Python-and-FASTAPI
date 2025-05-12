# List comprehension: Makes a whole list of squares
squares_list = [x * x for x in range(1, 6)]
print("List comprehension:", squares_list)  # Output: [1, 4, 9, 16, 25]

# Generator expression: Makes squares one by one
squares_generator = (x * x for x in range(1, 6))
print("Generator expression:", squares_generator)  # Output: <generator object <genexpr> at 0x...>

# Let's get the squares from the generator
print("Generator squares:")
for square in squares_generator:
    print(square)  # Output: 1, 4, 9, 16, 25

# Trying to print the generator again will print nothing.
squares_generator2 = (x * x for x in range(1, 6))
print("Generator squares again:")
for square in squares_generator2:
  print(square)

#Let's check the memory usage.

import sys

large_list = [x*x for x in range(1, 1000000)]
large_generator = (x*x for x in range(1, 1000000))

print(f"Size of large list: {sys.getsizeof(large_list)}")
print(f"Size of large generator: {sys.getsizeof(large_generator)}")