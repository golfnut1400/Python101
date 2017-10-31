
# use
fruit = "apple"
for idx in range(5):
    currentChar = fruit[idx]
print(currentChar)
print fruit.index('p')

print

fruit = "apple"
for idx in range(len(fruit)):
    print(fruit[idx])

print



fruit = "apple"
for idx in range(len(fruit)-1, -1, -1):
    print(fruit[idx])
print


s = "python rocks"
for idx in range(len(s)):
    if idx % 2 == 0:
        print(s[idx])

print


# prints out both index and value
fruit = "apple"
for idx in range(len(fruit)):

    print idx, ':', fruit[idx]


