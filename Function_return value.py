
def square(x):   # this is the function named square
    y = x * x
    return y      # 100. Sends value back to the code that called he function line 7

toSquare = 10    # set toSquare equal 10
result = square(toSquare)   #calls the square function and passes '10' to the function
print("The result of", toSquare, "squared is", result)
