
# for loop

def sumTo(aBound):
    theSum = 0
    for aNumber in range(1, aBound + 1):
        theSum = theSum + aNumber

    return theSum

print("The for loop returns theSum of:"),sumTo(4)

print(sumTo(1000))

# ----------------------------------------
# while loop
# ----------------------------------------
print
print

def sumTo(aBound):  # 4 is equal to the aBound
    """ Return the sum of 1+2+3 ... n """

    theSum  = 0
    aNumber = 1  #number of times gone through the loop
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1  #tracks the number of times it has gone through the loop
    return theSum

print("The while loop returns theSum of:"),sumTo(4)

print(sumTo(1000))
