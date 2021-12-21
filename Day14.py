'''
Higher Lower Game 
Let's see who has more number of followers
'''



# For Clearing screen after a person enters an amount so that it remains anonymous
import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

import random
from game_data import data
from art import logo,vs

def data_format(account):
  account_name=account["name"]
  account_desc=account["description"]
  account_country=account["country"]
  return f"{account_name}, {account_desc} from {account_country}"


def check_answer(guess,follower_count_A,follower_count_B):
  if follower_count_A>follower_count_B:
    return guess=="a"
  else :
    return guess=="b"

score=0
should_continue=True
account_B=random.choice(data)
print (logo)


while should_continue:
  

  account_A=account_B
  account_B=random.choice(data)

  while account_A==account_B:
    account_B=random.choice(data)

  print(f"\nCompare A : {data_format(account_A)}")
  print(vs)
  print(f"Against B : {data_format(account_B)}")
  guess=input("Who has more followers 'A' or 'B'?\nType 'A' or 'B'\n->Your Choice : ").lower()

  follower_count_A=account_A["follower_count"]
  follower_count_B=account_B["follower_count"]

  is_correct=check_answer(guess,follower_count_A,follower_count_B)

  # Waiting for 1 seconds to clear screen
  sleep(1)
  # Calling function we defined above for clearing the screen 
  screen_clear()
  print (logo)

  if is_correct:
    score+=1
    print(f"\nCorrect!!!!\nCurrent Score : {score}")
  else :
    should_continue=False
    print(f"\nOOPS, That's Wrong!!!\nFinal Score : {score}")
