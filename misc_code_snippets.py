"""
# Example of how to flatten embedded arrays/lists
arr = [[1,2], [3,4], [5,6]]
flat = []
for sub in arr:
    for x in sub:
        flat.append(x)

# Another way to do the above and flatten a list
# Fast and efficient with small lists, but large lists this is extremely slow
flat = sum(arr, [])
print(arr)
print(flat)
============================================================================
"""


# Store Fibonacci numbers in a list
fib = []
a, b = 0, 1
# Creates the fibonacci numbers
for _ in range(20):
    fib.append(a)
    a, b = b, a + b
print(fib)
"""
==================================
"""



