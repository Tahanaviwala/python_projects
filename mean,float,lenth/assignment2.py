# TODO put your name and additional information here

import sys

# TODO document the functions according the department standards


# TODO complete this function that takes a list of floating point numbers as a
# parameter and returns the mean
x = []
data = open('f1.dat', 'r')
for y in data.read().split('\n'):
    if y.isdigit():
        x.append(float(y))

def mean(numbers):
    total = sum(numbers)
    total = float(sum(numbers))
    return total / len(numbers)


print("Mean of a data is:" , mean(x))
a = mean(x)
# TODO complete this function that takes a list of floating point numbers as a
# parameter and returns the range
x = []
file_in = open('f1.dat', 'r')
for y in file_in.read().split('\n'):
    if y.isdigit():
        x.append(float(y))
    file_in.close()

def length(numbers):
    total = sum(numbers)
    total = float(sum(numbers))
    return len(numbers)


print("Length of a data is:" , length(x))

# TODO complete this function that takes a list of floating point numbers as a
# parameter and returns the variance


z = []
file_in = open('f1.dat', 'r')
for y in file_in.read().split('\n'):
    if y.isdigit():
        z.append(float(y))
    file_in.close()

def var(numbers):
    total = sum(numbers)
    total = float(sum(numbers))
    m = a
    var_res = sum((xi - m) ** 2 for xi in z) / len(z)
    return var_res

print("Variance of data is:" , var(z))

# TODO complete this function that takes a string representing a file name as a
# parameter and returns a list of floating point numbers read from an input
# file that contains one number per line. If the file does not exist or the
# file contains non-floating point data, then return an empty list

x = []
z = []


def get_data(filename):
    try:
        file_in = open(filename, 'r')
        for y in file_in.read().split('\n'):
            if y.isdigit() == False:
                x.append(y)
            elif y.isdigit():
                z.append(y)
            else:
                return x
        return x
    except FileNotFoundError:
        return x
get_data("f1.dat")
x = [i for i in x if i]
z = [i for i in z if i]
print("Float list of a data is:" , x)


def main():
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " <filename>")
        sys.exit(0)
    data = get_data(sys.argv[1])
    if data:
        # TODO print the mean, range, and variance
        print("Mean of the data is" + mean(a))
        print("Range of the data is" + rng(b))
        print("Variance of the data is" + var(c))
        return 'done'


# DO NOT EDIT ANYTHING BELOW THIS LINE
if __name__ == '__main__':
    main()  # call the main function
