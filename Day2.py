#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Welcome message 
print("Welcome to the tip Calculator.")

#Asking for total bill
bill=float(input("What was the total bill? $"))

#Asking for % tip
tip=float(input("What percentage of tip would you like to give? 10, 12, Or 15? "))

#Asking for people the bill is to be split between
split=float(input("How many people to split the bill? "))

#Calculating the total amount with the tip
p1=(bill*tip/100)+bill

#Splitting the bill and rounding of to two decimal places
ans= "{:.2f}".format(p1/split)

#Final Answer
print(f"Each person should pay : ${ans}")