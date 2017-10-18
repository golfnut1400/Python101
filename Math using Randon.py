import random

#use of range()
prob = random.random()
print(prob)

# use of randrange()
diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)


a = random.randrange(0, 101, 2)                 # Even integer from 0 to 100 inclusive
print (a)

print
print
# print 10 random numbers between 25 and 35, inclusive

import random

howmany = 10
for counter in range(howmany):
    arandom = random.randrange(26,34)
    print(arandom)
