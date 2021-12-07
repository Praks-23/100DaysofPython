'''
Blind Auction/Secret Auction
Code : https://replit.com/@praks23/blind-auction-start#main.py

'''



print(
    '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
)


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
  
# Defining a dictionary to store the names of person and their corresponding bids
bid={}

# Defining a while loop so the process can repeat for more users
state="yes"
while state=="yes":  
  name=input("Enter your Name : ")
  price=int(input("Enter your Bid Price : $"))
  # Storing the name and price in the dictionary
  bid[name]=price  
  #Checking for more bidders
  state=input("\nAre there any other bidders :\nType 'Yes' or 'No'\nYour Choice : ").lower()
  # Waiting for 1 seconds to clear screen
  sleep(1)
  # Calling function we defined above for clearing the screen 
  screen_clear()

# Checking for the highest bidder
highest_bid=1
winner=""
for names in bid:
  if bid[names]>highest_bid:
    highest_bid=bid[names]
    winner=names

# Printing the winner
print('''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
''')
print(f"The Winner is {winner.upper()} with a bid of ${highest_bid}.")