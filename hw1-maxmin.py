# James Moore

# Finds maximum value in an array by iterating through the array and comparing each value to the previous value
# The maximum element is then printed as a string
def max(numbers):
    for i in range(len(numbers)):
        if i == 0:
            maximum = numbers[i]
        elif i > 0 and numbers[i] > maximum:
            maximum = numbers[i]
    print("Maximum element: " + str(maximum))

# Finds minimum value in an array, and works in a similar manner to the max function
# The minimum element is printed
def min(numbers):
    for i in range(len(numbers)):
        if i == 0:
            minimum = numbers[i]
        elif i > 0 and numbers[i] < minimum:
            minimum = numbers[i]
    print("Minimum element: " + str(minimum))

def read():
    file = open("inputHW1.txt", "r") 
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values



numbers = read()

max(numbers)
min(numbers)
