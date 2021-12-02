'''
Rock Paper Scissors

Rules :
The outcome of the game is determined by 3 simple rules:
-Rock wins against scissors.
-Scissors win against paper.
-Paper wins against rock.
'''


import random

# ASCII art for Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



print("************************************* WELCOME TO THE ROCK-PAPER-SCISSORS GAME *************************************\n")
# Asking User for their input
user_choice=input("What do you choose?\n Type:\n 0 for Rock\n 1 for Paper\n 2 for Scissors.\nYour Choice : ")
# Printing the ASCII art according to the choice from the user
if user_choice=='0' :
  print(rock)
elif user_choice=='1' :
  print(paper)
elif user_choice=='2' :
  print(scissors)
else :
  print("YOU CHOOSE AN INVALID NUMBER\n")


# Creating variables for computer to choose from
options_to_choose_from=['0','1','2']
# Using random function to randomly select one of the choices
computer_choice=random.choice(options_to_choose_from)
# Printing the ASCII art according to the choice from the Computer
print(f"Computer's Choice : {computer_choice}\n")
if computer_choice=='0' :
  print(rock)
if computer_choice=='1' :
  print(paper)
if computer_choice=='2' :
  print(scissors)

# Analysing who won according to rules of the game
if (user_choice=='0' and computer_choice=='2') or (user_choice=='1' and computer_choice=='0') or (user_choice=='2' and computer_choice=='1') :
  print("YOU WIN")
else :
  if (user_choice=='0' and computer_choice=='0') or (user_choice=='1' and computer_choice=='1') or (user_choice=='2' and computer_choice=='2') :
    print("IT'S A DRAW")
  else :
    print("YOU LOSE")
  