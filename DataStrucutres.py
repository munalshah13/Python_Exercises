# Data Strcutre in Python

vangurd = ['Google', 'Alphabets','Microsoft','yahoo', 'Tesla']
print(vangurd[0])
#useful functions for list
print(len(vangurd)) # return how many elements are in the lsit
print(max(vangurd)) #return the gretest element of the list
print(min(vangurd)) # return the smallest element in a list
print(sorted(vangurd))  # return a copy of alist in order from smalles to largest


# Join method is a string method that takes a lsit of string as an argument, and return a string consisting of the list elements joined by a separator string
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

# Append method adds an element to the end of a list
vangurd.append('Amazon')
vangurd.append('Amazon')
print(vangurd)

# tuple
dimensions = 52,40,100    # tuple unpacking
length, width, height = dimensions  # tuple unpacking

print("The dimensions are {} x {} x {}".format(length, width, height))


"""
Set: is a data type for mutable unordered collections of unique elements
     is to quickley remove elements
    

list = set(vangurd)
print(list)

# you can add element using the add method

fruits = {"apple", "banana", "orange"}
print("Watermalon" in fruits)
fruits.add("watermelon")
print(fruits)

# remove a random element
fruits.pop()
print(fruits)
"""
"""
 what is, and When to use Disctionary?
 A Dictionary is a mutable data type that store mappings of unique keys to values.
 Dictionaries can have keys of any immutable type.

 Where is store data as key and value associate
 """
# Add vlaue mapped to vangurd varaible

vangurd = {}
vangurd["Alphabets"] = 3000
vangurd["Google"] = 2000
vangurd["Microsoft"] = 600
vangurd["Yahoo"] = 200 
vangurd["Tesla"] = 1000
vangurd["Amazon"] = 2500
print(vangurd)
print(vangurd.pop("Amazon"))
print("Amazon" in vangurd)
print(vangurd.get("Tesla"))
print(vangurd)

