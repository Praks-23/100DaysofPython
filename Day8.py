'''
Caeser Cipher
Here you can encode or decode your text.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# Printing the logo of the caeser cipher
print(logo)


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""

  # If the user wants to decode a text, then we will multiply the shift parameter by -1 so that instead of adding it will subtract from the list
  if cipher_direction == "decode":
    shift_amount *= -1
  
  for char in start_text:
    # Checking whether the entered character is present in the list or not
    # If present,the if statement will update it's position otherwise, it'll be kept as it is
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else :
      end_text+=char

  # Printing the final Output
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Adding a while loop to check whether the user wants to continue using the program or exit
answer="yes"
while answer=="yes":
  direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  answer=input("\n\nDo you want to Continue?\nType 'Yes' to continue\nType 'No' to end\n\nYour Choice : ").lower()

print("\n*****\nEND\n*****\n")


