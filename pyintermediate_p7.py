# Enumerate function returns tuple of the count along the way, and the item itself
# Use it on an iterable
import timeit


example = ['left', 'right', 'up', 'down']

# Wrong way, basically, if you ever come across a situation where you do this, use enumerate instead
for i in range(len(example)):
    print(i, example[i])

# Should to this
for i, j in enumerate(example):
    print(i, j)

""" # Proof that range(len()) is slower
print(timeit.timeit('''example = ['left', 'right', 'up', 'down']
for i in range(len(example)):
    print(i, example[i])''', number=5))

# Proof that enumerate is faster
print(timeit.timeit('''example = ['left', 'right', 'up', 'down']
for i, j in enumerate(example):
    print(i, j)''', number=5)) """

# Dictionary of key and index pairs built using enumerate from example
new_dictionary = dict(enumerate(example))
print(new_dictionary)

# No need to do this, but you can do so if need be
[print(i, j) for i, j in enumerate(new_dictionary)]

