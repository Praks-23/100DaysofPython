'''
Treasure Island Game
Making a "Choose Your Own Adventure" game using conditionals such as if, else, and elif statements to lay out the logic and the story's path in the program.
'''

#Printing a fun ASCII art along with a welcome message
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Taking input for the first stage of the game and converting it into lower case so that our code runs successfully irrespective of the case of input from the user.
stage1=input("This games starts at a crossroad\nWhich path do you want to choose : Left or Right ? \n").lower()
#In Stage 1, if the user selects left, then the game will continue.
if stage1=='left' :
  #Taking input for the stage 2 of the game and converting it into lower case.
  stage2=input("You've come to a lake. There is an island in the middle of the lake.\nDo you want to Swim to the island or Wait for the Boat.\nType 'Wait' to wait for a boat.\nType 'Swim' to swim across \n").lower()
  #In Stage 2, if the user selects wait, then the game will continue.
  if stage2=='wait' :
    #Taking input for the stage 3 of the game and converting it into lower case.
    stage3=input("You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and one blue.\nWhich colour do you choose?\n").lower()
    #In Stage 3, if the user selects yellow, then the user Wins.
    if stage3=='yellow':
      print("*************************************\nYOU WIN\n*************************************")
    #In Stage 3, if the user selects red or blue, then the user Loses.
    else :
      print("You enter a room of beasts.\nYou are dead\n**********************\nGAME OVER\n***********************")
  #In Stage 2, if the user selects swim, then the game is over.
  else :
    print("Tou were eaten by a crocodile in the pond.\n**********************\nGAME OVER\n***********************")

#In Stage 1, if the user selects right, then the game is over.
else :
  print("There was a Bear in the Bush\n You are Dead \n **********************\n GAME OVER \n ***********************") 

