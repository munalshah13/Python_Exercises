# Creating a histogram from a list of values

values = []

#input 10 values from user

print("please enter 10 integers:")

for i in range(10):
    newValue = int(input("Enter integer % d:" % (i + 1)))
    values += [newValue]
print(values)

# create histogram
print ("\nCreating a histogram from values:")
print("%s %10s %10s" % ("Element", "Values", "Histogram"))

for i in range(len(values)):
    print("%7d %10d %s" %(i, values[i], "*" * values[i])) # uses the multiplication operator(*) to create a string with the number of asterisks specifield by values[i]



"""

Creating a histogram from values:
Element     Values  Histogram
      0         10 **********
      1          9 *********
      2          8 ********
      3          6 ******
      4          5 *****
      5          4 ****
      6          3 ***
      7          2 **
      8          1 *
      9          0 


"""

