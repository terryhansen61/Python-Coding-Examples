num = 7

for i in range(num):
    #print('*')          # Prints a straight line, one on each line
    #print('*' * i)       # Prints a left sided triangle
    #print(' ' * (num - i - 1), '*' * i)     # Prints a right sided triangle
    print(' ' * (num - i - 1), '*' * (2 * i - 1))   # Prints a Christmas tree triangle
