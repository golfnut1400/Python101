"""
.

Method	Parameters	Description
upper	none	Returns a string in all uppercase
lower	none	Returns a string in all lowercase
capitalize	none	Returns a string with first character capitalized, the rest lower
strip	none	Returns a string with the leading and trailing whitespace removed
lstrip	none	Returns a string with the leading whitespace removed
rstrip	none	Returns a string with the trailing whitespace removed
count	item	Returns the number of occurrences of item
replace	old, new	Replaces all occurrences of old substring with new
center	width	Returns a string centered in a field of width spaces
ljust	width	Returns a string left justified in a field of width spaces
rjust	width	Returns a string right justified in a field of width spaces
find	item	Returns the leftmost index where the substring item is found, or -1 if not found
rfind	item	Returns the rightmost index where the substring item is found, or -1 if not found
index	item	Like find except causes a runtime error if item is not found
rindex	item	Like rfind except causes a runtime error if item is not found
format	substitutions	Involved! See String Format Method, below


"""
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)


print ('*****' * 5)



ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***" + ss.strip() + "***")
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")

news = ss.replace("o", "***")
print(news)

print ('*****' * 5)


food = "banana bread"
print(food.capitalize())

print("*" + food.center(25) + "*")
print("*" + food.ljust(25) + "*")     # stars added to show bounds
print("*" + food.rjust(25) + "*")

print(food.find("e"))
print(food.find("na"))
print(food.find("b"))

print(food.rfind("e"))
print(food.rfind("na"))
print(food.rfind("b"))

print(food.index("e"))

print ('*****' * 5)


#strings-5-2: What is printed by the following statements?
s = "python rocks"
print(s[1] * s.index("n"))



print ('***** String format' * 5)

person = raw_input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)

person = raw_input('Enter your name: ')
print('Hello {}!'.format(person))

origPrice = float(raw_input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)

a = 5
b = 9
setStr = 'The set is {{{}, {}}}.'.format(a, b)
print(setStr)

print ('*****' * 5)

# What is printed by the following statements?
v = 2.34567
print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))


