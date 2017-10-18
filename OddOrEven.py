"""
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Odd Or Even
input if types int equality comparison numbers mod
Again, the exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Exercise 2 (and Solution)

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
Discussion

Concepts for this week:

Modular arithmetic (the modulus operator)
Conditionals (if statements)
Checking equality
"""

num = int(raw_input("Enter a number:- "))
# if type(num) != int:
#     print ("You did not enter a number. Try again")

if num % 2 == 0:
    print ("The number you entered is an even number")
else:
    print ("The number you entered is an odd number")

# this is another way to solve

num = input("Enter a number: ")
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")

# this is another way to solve

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")


# this is another way to solve
if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)

