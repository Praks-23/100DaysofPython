'''
Coffee Machine
'''


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit = 0


def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please Insert Coins : ")
    total = int(input("Enter Quarters : ")) * 0.25
    total += int(input("Enter Dime : ")) * 0.1
    total += int(input("Enter Nickles : ")) * 0.05
    total += int(input("Enter Pennies : ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not Enough Money\nMoney Refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    user_choice = input(
        "What would you like :\n- Latte\n- Espresso\n- Cappuccino\n- Report(to get resource values)\n- OFF\nYour "
        "Choice : ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
