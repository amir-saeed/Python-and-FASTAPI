import copy

# Nested list (like a toy box with toys inside)
original_list = [1, 2, [3, 4]]

# Shallow copy
shallow_copy = copy.copy(original_list)

# Deep copy
deep_copy = copy.deepcopy(original_list)

# Let's change something in the original list
original_list[2][0] = 5  # Change the first element of the nested list

print("Original list:", original_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)