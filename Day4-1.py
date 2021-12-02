'''
Banker Roulette
We are writing a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
Important: We are not allowed to use the choice() function.
'''

import random

# Split string method
# It splits the string names_string into individual names and puts them inside a List called names.
names_string = input("Give me everybody's names, separated by a comma and space. ")
names = names_string.split(", ")
# Checking the total number of people entered
total_persons=len(names)
# Selecting a random name from the entered names
person_to_pay_bill=random.randint(0,total_persons-1)
print(f"{names[person_to_pay_bill]} is going to buy the meal today!")

