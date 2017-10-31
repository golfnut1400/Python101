
# program will ask user to enter 'Y' or 'No' and checks input

# function that is called by the statement below. if input ('Y' or 'No') is not entered
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = raw_input(message) # captures the users response
        answer = answer.upper() # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer

response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')  # calls 'get_yes_or_no' function and assigns to 'response' variable

if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')
