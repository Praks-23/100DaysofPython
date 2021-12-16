'''
Password Generator Project
Taking Input from the user for the number of letters, symbols or numbers they want in their password and then generating a random password.
'''


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Welcome message and asking user for the input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Defining a password list
password_list = []

# Taking random characters from the letters list mentioned above
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

# Taking random characters from the symbols list mentioned above
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

# Taking random characters from the numbers list mentioned above
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# We will use shuffle() to randomize the order of characters in the list 
random.shuffle(password_list)

# To print it together, we are converting it to a string
password = ""
for letter in password_list:
  password += letter

# Final Output
print(f"Your password is: {password}")
