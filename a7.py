"""
File: a7.py

"""

# James Moore 

from stack import Stack

def isPalindrome(sentence):
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack() # Creates a stack called stk.
    #Removes spaces and capitals from sentence and defines a list of allowed characters. Also defines a string for
    #later removal of special characters.
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    include = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    fixed_sentence = ""

    #Pushes all characters in sentence into the stack if character is allowed. Also appends character to end of
    #string for removal of special characters.
    for i in sentence:
        if i in include:
            stk.push(i)
            fixed_sentence += i

    #The string defined here is used in the loop below. Each popped value is appended to the string.
    reversed_sentence = ""
    for i in range(stk.size()):
        reversed_sentence += stk.pop()

    #True/false condition for the palindrome.
    if reversed_sentence == fixed_sentence:
        return True
    else:
        return False

def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")

main()
