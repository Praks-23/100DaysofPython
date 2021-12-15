'''
Hangman Game
'''

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''



import random

# importing wordlist and stages of hangman
from Day7-wordlist_hangman import word_list
from Day7-stages_hangman import stages

# Printing our game ASCII art
print(logo)

# Choosing a random word from the wordlist given 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


# Create blanks in place of words
display = []
for _ in range(word_length):
    display += "_"

# Asking user for letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # If the user has entered a letter they've already guessed, print the letter.
    if guess in display:
      print(f"You have already guessed '{guess}'")
    
    #Checking the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Checking if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and inform the user.
        print(f"'{guess}' is not present in the word.\nYou lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\n********************\nYou lose\n********************")

    # Joining all the elements in the list and turning it into a String.
    print(f"{' '.join(display)}")

    # Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\n********************\nYou Win\n********************")

    # Printing out the various stages of hangman.
    print(stages[lives])


                                                   
