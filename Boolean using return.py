def isDivisible(x, y):
    if x % y == 0:
        result = True
    else:
        result = False

    return result  # returns the value back to the calling statement below

print(isDivisible(10, 5))   # calls the isDivisibe() function and passes 2 arguments
