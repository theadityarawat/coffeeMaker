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
    "money": 0
            }


def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")


run = True


def check(drink):
    if drink == 'espresso':
        if MENU[drink]['ingredients']['water'] < resources['water']:
            if MENU[drink]['ingredients']['coffee'] < resources['coffee']:
                ask(drink)
            else:
                print("Sorry, we're running out of resources")
        else:
            print("Sorry, we're running out of resources")
    else:
        if MENU[drink]['ingredients']['water'] < resources['water']:
            if MENU[drink]['ingredients']['milk'] < resources['milk']:
                if MENU[drink]['ingredients']['coffee'] < resources['coffee']:
                    ask(drink)
                else:
                    print("Sorry, we're running out of resources")
            else:
                print("Sorry, we're running out of resources")
        else:
            print("Sorry, we're running out of resources")


def ask(drink):
    print("Please enter the coins: ")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))

    def total(q, d, n, p):
        return (q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01)-MENU[drink]['cost']

    if total(quarters, dimes, nickles, pennies) >= 0:
        print(f"Processing your order. Here is your {round(total(quarters,dimes,nickles,pennies),2)} change.")
        accept(drink)
    else:
        print("Sorry, but the money is insufficient. Giving a refund.")


def accept(drink):
    if drink != 'espresso':
        resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    resources['money'] += MENU[drink]['cost']
    print(f"Order completed. Here is you {drink.title()}. Enjoy")

while run:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice == 'report':
        report()
    elif choice == 'off':
        break
    else:
        check(choice)
