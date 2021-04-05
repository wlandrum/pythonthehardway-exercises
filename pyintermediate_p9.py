import timeit

# Generator function
def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'

for i in simple_gen():
    print(i)

# Better than a for loop or list comprehension
CORRECT_COMBO = (3, 6, 1)

# Must add this to break but this is faster than the below statement
found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo: {}'.format((c1, c2, c3)))
                found_combo = True
                break # doesn't really help
            print(c1, c2, c3)

# A lot cleaner and get to use generator to not waste memory
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        #print('Found the combo: {}'.format((c1, c2, c3)))
        break
    print(c1, c2, c3)
