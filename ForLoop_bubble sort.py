

# bubble sort
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1): # rem 'len(n(list) is the 'Start - 1', '0' is the Stop, -1 is the Step
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]

bubbleSort(nlist)  #calls the function

print(nlist)
