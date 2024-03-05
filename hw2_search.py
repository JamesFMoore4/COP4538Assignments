# James Moore

# Accepts list of values and key, searches through every value until key is found and increments # of attempts on each
# iteration
def linear_search(user_list, num):
    attempts = 0
    for i in user_list:
        attempts += 1
        if i >= num:
            return attempts
    return attempts

# Accepts list of values and key, searches through sorted list by halving the list each time based on whether the
# middle value is greater than or equal to the key and increments # of attempts on each iteration
def binary_search(user_list, num):
    attempts = 0
    low = 0
    high = len(user_list) - 1

    while high >= low:
        attempts += 1
        mid = (high + low) // 2
        if user_list[mid] < num:
            low = mid + 1
        elif user_list[mid] > num:
            high = mid -1
        else:
            return attempts
    return attempts

# Accepts name of file and splits values in file into a list
def read(file_name):
    file = open(file_name, "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

# Calls read and search functions, prints search key, # of attempts, and avg # of attempts
def main():
    sorted_linear = read("sortedLinearInput1.txt")
    sorted_binary = read("sortedBinaryInput1.txt")
    key_linear = read("keyLinear1.txt")
    key_binary = read("keyBinary1.txt")

    sorted_linear2 = read("sortedLinearInput2.txt")
    sorted_binary2 = read("sortedBinaryInput2.txt")
    key_linear2 = read("keyLinear2.txt")
    key_binary2 = read("keyBinary2.txt")

    print("Test 1:\n")

    avg_attempts = 0
    for i in range(len(key_linear)):
        num_attempts = linear_search(sorted_linear, key_linear[i])
        avg_attempts += num_attempts
        print("Search key: " +  str(key_linear[i]) + " Number of attempts: " + str(num_attempts))
    avg_attempts = avg_attempts / len(key_linear)
    print("Average number of attempts: " + str(avg_attempts) + "\n")

    avg_attempts = 0
    for i in range(len(key_binary)):
        num_attempts = binary_search(sorted_binary, key_binary[i])
        avg_attempts += num_attempts
        print("Search key: " + str(key_binary[i]) + " Number of attempts: " + str(num_attempts))
    avg_attempts = avg_attempts / len(key_binary)
    print("Average number of attempts: " + str(avg_attempts))

    print("\nTest 2:\n")

    avg_attempts = 0
    for i in range(len(key_linear2)):
        num_attempts = linear_search(sorted_linear2, key_linear2[i])
        avg_attempts += num_attempts
        print("Search key: " + str(key_linear2[i]) + " Number of attempts: " + str(num_attempts))
    avg_attempts = avg_attempts / len(key_linear2)
    print("Average number of attempts: " + str(avg_attempts) + "\n")

    avg_attempts = 0
    for i in range(len(key_binary2)):
        num_attempts = binary_search(sorted_binary2, key_binary2[i])
        avg_attempts += num_attempts
        print("Search key: " + str(key_binary2[i]) + " Number of attempts: " + str(num_attempts))
    avg_attempts = avg_attempts / len(key_binary2)
    print("Average number of attempts: " + str(avg_attempts))

main()
