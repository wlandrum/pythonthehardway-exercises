# Timeit module calculates the amount of time it takes for a segment of code to run
# Must put all the code into timeit paramater pass because it does it's own seperate process independant of your code
import timeit

""" input_list = [100]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# Generator
xyz = (i for i in input_list if div_by_five(i))

# List comprehension
xyz = [i for i in input_list if div_by_five(i)] """

# Generator
print(timeit.timeit('''input_list = [100]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# Generator
xyz = (i for i in input_list if div_by_five(i))''', number=5000))

# List comprehension
print(timeit.timeit('''input_list = [100]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# Generator
xyz = [i for i in input_list if div_by_five(i)]''', number=5000))

