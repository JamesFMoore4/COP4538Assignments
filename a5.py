# James Moore 

"""
File: a5.py
Assignment 5

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.
"""

from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0

    
    if probe != None:
        for i in probe:
            count += 1
    
    return count
    
def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""
    newItem = Node(newItem)

    if head == None:

        head = list()
        head.append(newItem)

    else:

        for i in range(length(head)):

            alias1 = newItem.data
            alias2 = head[i].data

            if alias1.lower() > alias2.lower():
                if i == length(head) - 1:
                    head.append(newItem)
                    head[i].next = newItem
                    break
                else:
                    continue
            else:
                if i == 0:
                    head.insert(0, newItem)
                    head[0].next = head[1]
                    break
                else:
                    head.insert(i , newItem)
                    head[i].next = head[i + 1]
                    head[i-1].next = head[i]
                    break

    return head

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    if head != None:
        for i in head:
            print(i.data, end = ' ')
    print()

def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""
    
    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)
        
    print('The structure contains', length(head), 'items:', end = ' ')
    printStructure(head)

if __name__ == "__main__": main()
