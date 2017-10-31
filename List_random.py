import random

L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
newlist = random.sample(set(L), 3) # where x is the number of samples that you want

print (newlist)



print
print


# new example

#first_list= random.sample(range(25),15)  #creates 15 random numbers up to 25
first_list = random.sample(set(L), 5) # where x is the number of samples that you want


L = []  #new empty list

L.append(first_list)

#newlist = random.sample(set(L), 3) # where x is the number of samples that you want

print (L)
