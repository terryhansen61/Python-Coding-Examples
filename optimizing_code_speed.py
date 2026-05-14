# This shows examples of ways to run code more efficiently with python
# Not that either way is wrong, but the optimized version runs a lot faster
# than the looping function call
import time

def inefficient_function(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result

def optimized_function(n):
    return (n * (n - 1) * (n - 1) * (n + 1)) // 4

start = time.time()
print(inefficient_function(10000))
end = time.time()
print('Inefficient: ', end - start)

start = time.time()
print(optimized_function(10000))
end = time.time()
print('Optimized: ', end - start)
