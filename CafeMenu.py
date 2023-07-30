print("  Cafe Menu....")
print("---------------")
print("1. Soup and salad")
print("2. Pasta with meat sauce")
print("3. Chef's special")
print("4. (Soup and Salad) + (Pasta with meat sauce)")
print()

menuselection = int(input("Which number would you like to order?"))
if menuselection == 1:
    num = input("How many items?")
    print(int(num))
    print()
    print(" your order",num,"Soup and salad coming right up!")
if menuselection == 2:
    num = int(input("How many items?"))
    print()
    print(" your order",num,"Pasta with meat sauce coming right up!")
elif menuselection == 3:
    num = int(input("How many items?"))
    print()
    print(" your order",num,"Chef's special coming right up!")
elif menuselection == 4:
    num = int(input("How many Soup and Salad?"))
    num2 = int(input("How many Past with meat sauce"))
    add = num + num2
    print("your total item is:",add)
    print()
    print(" your order",add,"Soup and salad coming right up!")
else:
    print("Sorray, that is not a valid choice")
    
