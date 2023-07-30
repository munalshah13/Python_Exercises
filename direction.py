direction = input("Do you want to count up or down? (u/d):")
if direction == "u":
    num = int(input('Enter a top number'))
    for i in range(1, num +1):
        print(i)
elif direction == "d":
    num = int(input("Enter a number below 20:"))
    for i in range(20,num-1,-1):
        print(i)
else:
    print("I dont understand")
