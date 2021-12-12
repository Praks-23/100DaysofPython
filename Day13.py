'''
Life in Weeks
Creating a program that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take our current age as the input and output a message with our time left.
'''


age = input("Enter the current age : ")

age=int(age)
d=90*365
m=90*12
w=90*52

d1=age*365
m1=age*12
w1=age*52

print(f"You have {d-d1} days, {w-w1} weeks, and {m-m1} months left.")



