# James Moore

# Sets global variable of count to keep track of recursive function calls
count = 0


# Solves Tower of Hanoi Puzzle for N number of disks. Global variable count used to track function calls. If disk
# is 1, it can simply be moved. Otherwise, recursive calls are necessary. Print statements used to track movements.
def tower(disks, pole_from, pole_to, pole_spare):
    global count
    count += 1
    if disks == 1:
        print("Move disc 1 from source", pole_from, "to destination", pole_to)
        return
    else:
        tower(disks - 1, pole_from, pole_spare, pole_to)
        print("Move disc", disks, "from source", pole_from, "to destination", pole_to)
        tower(disks - 1, pole_spare, pole_to, pole_from)
    return count


# Takes input for number of disks, calls function, and prints count
num = int(input("Input length of the tower: "))
count = tower(num, 'A', 'C', 'B')
print("count = ", count)
