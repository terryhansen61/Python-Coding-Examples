# This can be used to count items in a list, dictionary, word, etc.
from collections import Counter

names = ['Adam', 'John', 'Peter', 'Harry', 'Peter', 'Adam', 'John', 'Mary', 'Robert', 'Alvin', 'Joe', 'John']
counts = Counter(names)
print(counts)
print(counts.most_common(3))
print(counts['Peter'])
print(counts.get('Alice', 0))
