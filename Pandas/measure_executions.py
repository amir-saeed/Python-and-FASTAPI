import timeit

# Code we want to time
my_code = """
total = 0
for i in range(1000):
    total += i
"""

# Time it!
time_taken = timeit.timeit(my_code, number=1000)

print(f"Time taken: {time_taken} seconds")