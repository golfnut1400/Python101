# shoutout = "We like Python's turtles!"
#
# count = 0
#
# if count <= 100:
#     count = count + 1
#     print (count)


# months = ['January','Febuary','March','April','May','June','July', 'August','September','October', 'November', 'December']
# for index in months:
#     print ("One of the months of the year is", index)

my_list = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for index in my_list:
    print (index)

print
print

for index in my_list:
    index = index **2
    print (index)


import turtle

wn = turtle.Screen()
lovelace = turtle.Turtle()

print type(lovelace)


s = "python rocks"
for idx in range(len(s)):
    if idx % 2 == 0:
        print(s[idx])


