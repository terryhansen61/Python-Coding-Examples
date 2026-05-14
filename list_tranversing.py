# traversing lists in Python

# Basic list traversal with for loop
numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    print(num)

# Traversing with Index using enumeration()
# When you need both the index and value
fruits =['apples','bananas','oranges','dates']
for idx, fruit in enumerate(fruits, start=1):
    print(f'{idx} : {fruit}')

# Traversing with a while loop - less common
numbers = [10,20,30,40,50,60,70,80,90]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

# Traversing with list comprehension
numbers = [1,2,3,4,5,6,7,8,9]
squares = [n**2 for n in numbers]
print(squares)

# Filter even numbers
evens = [n for n in numbers if n %2 == 0]
print(evens)