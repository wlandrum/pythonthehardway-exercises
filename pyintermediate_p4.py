# List comprehension and generator expressions

for i in range(5):
    print(i)


xyz = [i for i in range(5)]
print(xyz)

# What does this mean?
xyz = []
for i in range(5):
    xyz.append(i)
    print(xyz)

# List comprehension?
xyz = (i for i in range (5))
print(xyz)

# Generator object is printed so we must iterate over it
for i in xyz:
    print(i)

# Major difference is, the generator takes very little time to generate, but if you want to iterate over it, it will take along time to do so.



