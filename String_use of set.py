

#You are given 2 strings: string, strong. Find the common alphabets in two strings and print it.

# Solution using Python

list_a = set(["string", 'a'])
list_b =  set(["strong", "string", "a"])
#print (list_a.intersection(list_b))


#use for loop to iterate through list_a and list_b

for a, b in zip(list_a,list_b):
    if a == b:
        print (a)
    else:
        print (b)

set(list_a) and set(list_b)
print (set)




print ("Done")
