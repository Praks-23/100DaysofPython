'''
Calculator
'''


logo='''
 _____________________
|  _________________  |
| |              /  | |
| |       /\    /   | |
| |  /\  /  \  /    | |
| | /  \/    \/     | |
| |/             JO | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
calc_logo='''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
'''

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  if n2==0:
    return "Invalid"
  else:
    return n1/n2

def calculator():
  print(logo)
  print(calc_logo)

  num1=float(input("\nEnter the first number : "))

  operations={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
  }

  continue_operation = "yes"

  while continue_operation=="yes":
    for operator in operations:
      print(operator)
    operation_of_choice=input("Choose one of the above mentioned operations\nYour Choice : ")

    num2=float(input("Enter the next number : "))

    calc_function=operations[operation_of_choice]
    answer=calc_function(num1,num2)
    print(f"{num1} {operation_of_choice} {num2} = {answer} ")

    continue_operation=input("\nType 'Yes' to continue calculating with the previous answer\nType 'No' to start a new calculation\nYour Choice : ").lower()
    if continue_operation=="yes":
      num1=answer
    else :
      continue_operation="no"
      calculator() 

calculator()