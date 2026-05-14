# Using the IN operator
"""
numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]

if 5 in numbers:
    print('5 is present in the list')
else:
    print('5 is not present in the list')

if 9 in numbers:
    print('9 is present in the list')
else:
    print('9 is not present in the list')

if 10 in numbers:
    print('10 is present in the list')
else:
    print('10 is not present in the list')
"""
# Using the index().find the position of an element
"""
colors = ['Blue','Green','Red','Black','Yellow','Purple','Brown']

print(colors.index('Blue'))
print(colors.index('Green'))
"""

# Linear Searching
scores = [45,67,98,23,67]

target = 67
position = -1

for i in range(len(scores)):
    if scores[i] == target:
        position = i
        break

if position != -1:
    print(f'{target} found at index {position}')
else:
    print(f'{target} not found')

