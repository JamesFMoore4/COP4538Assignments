# James Moore 

# Accepts a list and uses a nested loop to check how many times each value in the list appears, adds # and its
# frequency into a tuple and then appends it into a new list, then adds the number to another list in order to avoid
# duplicates (each time the outer loop iterates, the program checks to see if the number is in the drop list)

def frequency(user_list):

    
    frequency_list = []
    drop_list = []

   
    for i in user_list:          
        if i not in drop_list:   
            fr = 0               
            for j in user_list:  
                if i == j:      
                    fr += 1      
            frequency_list.append((i,fr))    
            drop_list.append(i)              

    return frequency_list

# Accepts name of file and splits values in file into a list

def read(file_name):
    file = open(file_name, "r")        
    line = file.readline()             
    values = []                        
    for value in line.split(' '):     
        values.append(int(value))      
    return values

# The code below simply calls the read function and passes the created list into the frequency function, then prints
# all numbers in the list and their frequencies
num_list = read("frequency_nums1.txt")
num_list2 = read("frequency_nums2.txt")


for i in num_list:
    print(i, end = " ")
print("")


for i in num_list2:
    print(i, end = " ")
print("")

frequency_list = frequency(num_list)
frequency_list2 = frequency(num_list2)

print("\nTest 1:\n")
print("The frequency of the numbers: ", end = " ")

for i in frequency_list:
    print(i, end = " ")
print("")

print("\nTest 2:\n")
print("The frequency of the numbers: ", end = " ")

for i in frequency_list2:
    print(i, end = " ")


