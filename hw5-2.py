# James Moore 

from node import Node

#creates linked list from file
def read():

    file = open('hw5-2.txt', 'r')
    lines = file.readline().split(' ')
    values = []
    for i in range(len(lines)):
        lines[i] = Node(int(lines[i]))
        values.append(lines[i])
        if i != 0:
            values[i-1].next = values[i]
    values[0].next = values[1]

    return values

#splits array into two repeatedly, values are then compared and replace original values in array
def mergesort(head, size):

    if size == 1:
        return head

    split = size // 2
    left_head = head[:split]
    right_head = head[split:]

    count_left = 0
    count_right = 0
    for i in left_head:
        count_left += 1
    for i in right_head:
        count_right += 1

    mergesort(left_head, count_left)
    mergesort(right_head, count_right)

    i = 0
    j = 0
    k = 0
    while i < count_left and j < count_right :

        if left_head[i].data < right_head[j].data:
            head[k] = left_head[i]
            i += 1
            k += 1
        else:
            head[k] = right_head[j]
            j += 1
            k += 1

    while i < count_left:
        head[k] = left_head[i]
        i += 1
        k += 1

    while j < count_right:
        head[k] = right_head[j]
        j += 1
        k += 1

    final_count = 0
    for i in head:
        final_count += 1

    for i in range(final_count):
        if i < final_count - 1:
            head[i].next = head[i + 1]

    return head

#calls functions, counts length of list, and prints sorted values
def main():

    linked_list = read()

    count = 0
    if linked_list != None:
        for i in linked_list:
            count += 1

    linked_list = mergesort(linked_list, count)

    print("Sorted Values: ", end = '')
    for i in linked_list:
        print(i.data, end = ' ')

if __name__ == "__main__": main()