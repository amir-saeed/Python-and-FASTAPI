def count_to_three():
    yield 1
    yield 2
    yield 3

#Using the generator
for number in count_to_three():
    print(number) #prints 1, then 2, then 3.