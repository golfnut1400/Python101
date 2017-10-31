#
# Create a program that asks the user for a number and then prints out a list of all the divisors
# of that number.
# (If you do not know what a divisor is, it is a number that divides evenly into another number."""
#  For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num + 1))  # sets the range of the list

#listRange = list(range(0,1000))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print("These numbers can be divided envenly in another number", divisorList)

# another example

while True:
    try:
        x = int(input("Please enter a number: "))
        print("You entered", x)
        break
    except ValueError:
     print("Oops! That was no valid number. Try again...")


# another example

out=[]
#using list comprehension
out = [idx for idx in range(1,x,1) if x%idx==0]
print(out)
