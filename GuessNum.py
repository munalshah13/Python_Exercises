# Guessing a Number

import random

smaller = int(input('Enter Lower Num:'))
larger = int(input('Enter upper Num:'))
mynumber = random.randint(smaller, larger)

count  = 0
while True:
    count += 1
    userNum = int(input("enter your number:"))
    if userNum < mynumber:
        print("This is samller  number:")
    elif userNum > mynumber:
        print("larger number")
    else:
        print("you've got it in", count, "tries!")
        break


if __name__ == "__main__":
    main()
              
        

