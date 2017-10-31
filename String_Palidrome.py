
"""Task :
To check whether a number is palindrome or not

Approach :
Read an input number using input() or raw_input().
Check whether the value entered is integer or not.
We convert that integer number to string str(num).
Now we use advanced slice operation [start:end:step] leaving start and empty and giving step a value of -1, this slice operation reverses the string.
Now check whether reverse is equal to num,
If reverse is equal to num, the number is palindrome
When reverse is not equal to num, it is not a palindrome"""

num = raw_input('Enter any number : ')
try:
    val = int(num)
    if num == str(num)[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a palindrome')
except ValueError:
    print("That's not a valid number, Try Again !")



# another exmaple

string = raw_input("Enter string:")
if(string == string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")
