# With big list comprehension you will run out of memory
# With big generators you will run out of time
input_list = [5,6,1,2,7,8,20,15,3]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))

# logic for above generator
#xyz = []
#for i in input_list:
#    if div_by_five(i):
#        xyz.append(i)

for i in xyz:
    print(i)

# Different solution to above
[print(i) for i in xyz]

# list comprehension version
xyz = [i for i in input_list if div_by_five(i)]

# Generator object
# Not something that you will typically see
(print(i) for i in xyz)

# List comprehension of every combination of number sets between 0 and 5
[[print(i, ii) for ii in range(5)] for i in range(5)]

# Logical representation of above statement (work backwards to achieve above statement)
for i in range(5):
    for ii in range(5):
        print(i, ii) 

# Tuples
xyz = [[(i, ii) for ii in range(5)] for i in range(5)]
print(xyz)

# List
xyz = [[[i, ii] for ii in range(5)] for i in range(5)]
print(xyz)

# Generator expression
xyz = (((i, ii) for ii in range(5)) for i in range(5))
print(xyz)

for i in xyz:
    for ii in i:
        print(ii)   

