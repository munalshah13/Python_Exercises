# Creating, accessing and changing a list

aList = [] # creating empty list

#add values to list
for numbers in range(1, 11):
    aList += [numbers]
    

print("The value of alist is:", aList)

# access list values by interation
print("\nAcessing values by iteration:")

for item in aList:
    print(item,)

print("   ")


# access list values by index
print("\nAccessing values by index:")
print("Subscript   values")

for i in range(len(aList)):
    print("%9d %7d" %(i, aList[i]))

# modify lsit
print("\nModifying a list value....")
print("Value of aList before modification:", aList)
aList [0] = -100
aList [-3] = 19

print("Value of aList after modification:", aList)

#Output

"""
Accessing values by index:
Subscript   values
        0       1
        1       2
        2       3
        3       4
        4       5
        5       6
        6       7
        7       8
        8       9
        9      10

Modifying a list value....
Value of aList before modification: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Value of aList after modification: [-100, 2, 3, 4, 5, 6, 7, 19, 9, 10]

"""
