# James Moore 

# Functions readm1() and readm2() simply read in m1.txt and m2.txt
def readm1():
    file = open("m1.txt", "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)
    return a

def readm2():
    file = open("m2.txt", "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)
    return a

# Accepts two matrices, then declares an array to store sum matrix. If matrix dimensions do not match, program
# is terminated. A nested for loop is used for the addition, and an additional nested for loop is used to print
# the matrix as a grid.
def entrywise_sum(a, b):

    c = list()

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Matrix size dismatch")
    else:
        for i in range(len(a)):
            d = []
            for j in range(len(a[0])):
                value = a[i][j] + b[i][j]
                d.append(value)
            c.append(d)
        for i in range(len(c)):
            for j in range(len(c[0])):
                print(c[i][j], end = " ")
            print("")


m1 = readm1()
m2 = readm2()

entrywise_sum(m1,m2)
