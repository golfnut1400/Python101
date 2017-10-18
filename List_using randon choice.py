import random


all_data = random.sample(range(1000),15)  #creates 15 random numbers up to 1000

#all_data = [1,2,2,3,4,5,6,7,8,8,9,10,11,11,12,13,14,15,15]  #hard coded list

choices = []

while len(choices) < 4:
    selection = random.choice(all_data)
    if selection not in choices:
        choices.append(selection)
print choices
