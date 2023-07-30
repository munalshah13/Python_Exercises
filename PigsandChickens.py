def solve(numLegs,numHeads):
    for numChicks in range(0, numHeads + 1):
        numPlgs = numHeads - numChicks
        totLegs = 4 *numPlgs + 2 *numChicks
        if totLegs == numLegs:
            return (numPlgs,numChicks)
    return(None, None)

def barnyard():
    heads = input("Enter number of heads: ")
    legs = input("Enter a number of legs: ")
    pigs, chickens = solve(int(heads),int(legs))
    if pigs == None:
        print("There is no solution ")
    else:
        print("Number of pigs:", pigs)
        print("Number of chickens:", chickens)
