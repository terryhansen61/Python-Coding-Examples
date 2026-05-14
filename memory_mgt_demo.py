# Create an object in memory and show the memory location of that object using ID
a=10
b=10
print(id(a), id(b))

# Reference counting - how many object references are there for x
import sys
x=[1,2,3]
print(sys.getrefcount(x))

# Multiple reference to same object
a=[1,2]
b=a
print(a is b)

# Object deletion
x=[1,2]
del x
print('x deleted')

# Garbage collection
import gc
print(gc.isenabled())

# Circular Reference
a=[]
a.append(a)
print('circular reference created')

# Manually trigger garbage collection
import gc
gc.collect()
print('GC run')

