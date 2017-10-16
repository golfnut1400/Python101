"""Exercise 1 Character Input

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""



from datetime import date
currentYear = date.today().year
print("========== Welcome to Century Calculator ==========")
print()
myName = raw_input("Enter your name here:- ")
myAge = int(raw_input("Enter your age here:- "))
countYears = (((currentYear - myAge) + 100) - currentYear)

print("'" + myName + "'", "has %d years to Century." %(countYears))
