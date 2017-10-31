

"""Program Explanation
1. User must enter a string.
2. The string is passed as an argument to a recursive function.
3. In the function, if the length of the string is less than 1, True is returned.
4. If the last letter is equal to the first letter, the function is called recursively with the argument as the sliced list with the first character and last character removed, else return False.
5. The if statement is used to check if the returned value is True or False and the final result is printed.

Runtime Test Cases

Case 1:
Enter string:mom
String is a palindrome!

Case 2:
Enter string:hello
String isn't a palindrome!"""




def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

a=str.lower(raw_input("Enter string:"))

if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
