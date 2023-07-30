compnum = 50
count = 1
guess = int(input("Enter your guess number here:"))
while guess != compnum:
    if guess < compnum:
        print("To Low")
    else:
        print("To high")
    count += 1
    guess = int(input("would you like to again guess number"))
    print("Well Done!")
