'''Blackjack Project

-> Blackjack House Rules
-The deck is unlimited in size. 
-There are no jokers. 
-The Jack/Queen/King all count as 10.
-The the Ace can count as 11 or 1.
-Use the following list as the deck of cards:
-cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
-The cards in the list have equal probability of being drawn.
-Cards are not removed from the deck as they are drawn.
'''

logo='''
                              _____
         _____                _____ |6    |
        |2    | _____        |5    || & & |
        |  &  ||3    | _____ | & & || & & | _____
        |     || & & ||4    ||  &  || & & ||7    |
        |  &  ||     || & & || & & ||____9|| & & | _____
        |____Z||  &  ||     ||____S|       |& & &||8    | _____
               |____E|| & & |              | & & ||& & &||9    |
                      |____h|              |____L|| & & ||& & &|
                                  _____           |& & &||& & &|
                          _____  |K  WW|          |____8||& & &|
                  _____  |Q  ww| | o {)|                 |____6|
           _____ |J  ww| | o {(| |o o%%| _____
          |10 & || o {)| |o o%%| | |%%%||A _  |
          |& & &||o o% | | |%%%| |_%%%>|| ( ) |
          |& & &|| | % | |_%%%O|        |(_'_)|
          |& & &||__%%[|                |  |  |
          |___0I|                       |____V|
'''


import random

# Creating a function to choose cards
def deal_card():  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Creating a function calculate_score() that takes a list of cards as input and returns the score.
def calculate_score(cards):    
  # Checking for a blackjack (a hand with only 2 cards: ace + 10)
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # Checking for an Ace(11). If the score is already over 21, then removing the 11 and replacing it with 1.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# Creating a function compare() to calculate scores
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "\n-------------\n!! YOU LOST !!\nYOU WENT OVER 21\n-------------"
  if user_score == computer_score:
    return "\n-------------\nDRAW\n-------------"
  elif computer_score == 0:
    return "\n-------------\n!! YOU LOST !!\nCOMPUTER HAS A BLACKJACK\n-------------"
  elif user_score == 0:
    return "\n-------------\n（￣︶￣） YOU WIN WITH A BLACKJACK （￣︶￣）\n-------------"
  elif user_score > 21:
    return "\n-------------\n!! YOU LOST !!\nYOU WENT OVER 21\n-------------"
  elif computer_score > 21:
    return "\n-------------\n（￣︶￣） YOU WIN （￣︶￣）\nCOMPUTER WENT OVER 21\n-------------"
  elif user_score > computer_score:
    return "\n-------------\n（￣︶￣） YOU WIN （￣︶￣）\n-------------"
  else:
    return "\n-------------\n!! YOU LOST !!\n-------------"

def game():

  print(logo)

  # Dealing 2 cards each using function deal_card() to user and computer
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())  

  while not is_game_over:
    # Calling calculate_score() to check the score of both user and computer
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Showing the cards of user and one card of computer
    print(f"\nYour Cards  : {user_cards}")
    print(f"Total Score : {user_score}")
    print(f"\nComputer's First card : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      # Asking the user whether they want to draw another card or not if the game has not ended already
      user_should_deal=input("\nType 'Yes' if you want to get another card\nType 'No' if you want to pass\nYour choice : ").lower()
      if user_should_deal == "yes":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  # Once the user is done, we will let the computer play
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  
  print(f"\nComputer's Final Deck: {computer_cards}\nFinal Score: {computer_score}\n")
  print(compare(user_score, computer_score))

print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
)

# Asking the user if they want to restart the game
while (input("\nDo you want to play a game of Blackjack?\nType 'Yes' or 'No': ").lower()) == "yes":
  game()
