names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    # more readable
    print('Hello there, ' + name)

    #high performance
    print(' '.join(['Hello there,', name]))

# use join if concatenating more than two strings because it will scale better with less processing
print(', '.join(names))

import os

location_of_files = 'C:\\VScode\\willprograms\\python_intermediate\\'
file_name = 'testfile.txt'

# not right way because it doesn't read content
print(location_of_files + "\\" + file_name)

# rigth way because it reads content
with open(os.path.join(location_of_files, file_name)) as f:
    # reads content
    print(f.read())


# string formatting
who = 'Gary'
how_many = 12

# Gary bought 12 apples today!

# incorrect way
print(who, 'bought', how_many, 'apples today!')
# correct way, and order matters on how you have the variables in the .format function
print('{} bought {} apples today!'.format(who, how_many))

