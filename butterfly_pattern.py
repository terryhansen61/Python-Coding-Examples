# Butterfly Pattern in Python
from cmath import phase

# Classic Butterfly
n = 4
for i in range(1, n+1): #loop rows
    left = '*' * i #left stars increase
    spaces = ' ' * (2*(n-i)) #spaces decreases
    right = '*' * i #right stars mirror left
    print(left + spaces + right) #combine and print

# Full Butterfly
n = 4

# Upper half + middle
n = 4
for i in range(1, n+1): #loop rows
    left = '*' * i #left stars increase
    spaces = ' ' * (2*(n-i)) #spaces decreases
    right = '*' * i #right stars mirror left
    print(left + spaces + right) #combine and print

# Lower half (mirror)
for i in range(n-1, 0, -1):
    left = '*' * i
    spaces = ' ' * (2*(n-i))
    right = '*' * i
    print(left + spaces + right)

# Animated Butterfly
import time
import os

n = 6

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

for phase in range(8):
    clear()
    for i in range(1, n+1):
        left = '*' * (i + (phase % 3))
        right = '*' * (i + ((phase + 1) % 3))
        spaces = ' ' * (2*(n-i))
        print(left + spaces + right)
    time.sleep(0.4)

