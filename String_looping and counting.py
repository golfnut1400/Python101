# count the number of 'a' in the string

#
# def count(text, aChar):
#     lettercount = 0
#     for c in text:
#         if c == aChar:
#             lettercount = lettercount + 1  # counter is the accumalator. count ther number of 'a'
#     return lettercount
#
# print("Letter count:",count("banana","a")) # calls function and passes 2 arguments. 'a' is the aCharc you want to finc and count

def count(text, aChar):
    letterCount = 0
    for c in text:
        if c == aChar:
            letterCount = letterCount + 1
    return letterCount



print(count("stanleay","a"))





