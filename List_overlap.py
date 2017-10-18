"""Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes."""


import random

#first_list= random.sample(range(15),8)

first_list= random.sample(range(25),15)  #creates 15 random numbers up to 25

second_list=random.sample(range(50),20)  #creates 50 random numbers up to 20

print first_list

print second_list

common_numbers= []    # new list and will be filled from statements below

for num in first_list:

    if num in second_list:

        common_numbers.append(num)

print common_numbers
