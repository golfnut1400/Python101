
# prints each character that is not a vowel

def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels = ""
    for eachChar in s:
        if eachChar not in vowels:  # check character not in the variable vowels
            sWithoutVowels = sWithoutVowels + eachChar  # accumulator
    return sWithoutVowels

print(removeVowels("compsci")) # calls function
print(removeVowels("aAbEefIijOopUus"))
