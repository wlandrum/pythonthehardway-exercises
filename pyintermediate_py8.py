# Zip function takes elements from multiple iterables and aggregates them into one, where the index value can be shared.

x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

# Tie x and y together
for a,b in zip(x,y):
    print(a,b)

# Tie x, y, z together
for a,b,c in zip(x,y,z):
    print(a,b,c)

# What is zip? Prints a zip object
print(zip(x,y,z))

# Iterate over, tuples of values
for i in zip(x,y,z):
    print(i)

# Convert zip to list
print(list(zip(x,y,z)))

# Convert zip to dict, but can only pass two values
print(dict(zip(x,y)))

# List comprehension
[print(a,b,c) for a,b,c in zip(x,y,z)]

