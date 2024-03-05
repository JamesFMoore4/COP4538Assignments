# James Moore

# Reads in input arrays.
def read(f):
    file = open(f, "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

# Binary search algorithm using recursion. If key is less than or greater than low or high values, program terminates.
# Else, array splits and function is again called until only one value is left. Value is then checked.
def binary_search(array, low, high, key):

    mid = (high + low) // 2

    if array[high] < key or array[low] > key:
        print("Binary Search by Recursive:")
        print("Cannot find the number!")
        return

    if array[mid] < key:

        return binary_search(array, mid + 1, high, key)

    elif array[mid] > key:

        return binary_search (array, low, mid - 1, key)

    print("Binary Search by Recursive:")
    if array[mid] != key:
        print("Cannot find the number!")
    else:
        print("Found number " + str(array[mid]) + " in place #" + str(mid + 1))


# Code below simply reads in files, takes input for search keys and calls functions above
test1 = read("test1.txt")
test2 = read("test2.txt")

key1 = int(input("Input search target value: "))
binary_search(test1, 0, len(test1) - 1, key1)

key2 = int(input("Input search target value: "))
binary_search(test2, 0, len(test2) - 1, key2)
