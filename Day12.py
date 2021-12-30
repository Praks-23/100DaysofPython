'''
Number Guessing Game
'''


logo='''
   _____                      _   _            _   _                 _               
  / ____|                    | | | |          | \ | |               | |              
 | |  __ _   _  ___ ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ / __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ | '__|
 | |__| | |_| |  __\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __| |   
  \_____|\__,_|\___|___|___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                                                                                       
'''

prize='''
                           
      (_v_)                   
       _|_                    
       | |                    
  |-----+-----|               
  |   WINNER  |                
  |           |                
   '---------'                  
    \       /                
     '.   .'                  
       | |                   
      .' '.                
     _|___|_                  
    [#######]            

'''

print(logo)

import random
print("\nWELCOME TO THE NUMBER GUESSING GAME")
print("\nThe number is between 1 and 100 ¯\_(ツ)_/¯")
level=input("\nThere are two levels: 'Easy' and 'Hard'\nType 'Easy' or 'Hard'\nYour Choice : ").lower()

def game_level():
  if level=="easy":
    return 10
  if level=="hard":
    return 5

tries=game_level()

num=int(random.randint(1,100))

count=-1

def guess_num(tries):
  print(f"\n-> You have {tries} chances to guess the Number")
  user_guess=int(input("Make a Guess : "))
  if user_guess==num:
    return 0
  elif user_guess>num:
    return 1
  else:
    return 2

while(tries!=0):
  count=int(guess_num(tries))
  if count==0:
    print(f"\nYou Got it!!\nYOU WIN")
    print(prize)
    break
  elif count==1:
    print(f"Your guess was higher than the number")
  else :
    print( f"Your guess was lower than the number")
  
  tries=tries-1
if(tries==0):
  print("\nYOU LOSE")

