from data import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
turn_off = False


def report():
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def check_resources(choice):
    check = True
    if choice != "espresso":
        if milk < MENU[choice]["ingredients"]["milk"]:
            print("Sorry, that's not enough milk.")
            check = False
    if water < MENU[choice]["ingredients"]["water"]:
        print("Sorry, that's not enough water.")
        check = False
    if coffee < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry, that's not enough coffee.")
    return check


def insert_money():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def coffee_choice(choice):
    global milk, water, coffee, money
    if choice != "espresso":
        milk -= MENU[choice]["ingredients"]["milk"]
    water -= MENU[choice]["ingredients"]["water"]
    coffee -= MENU[choice]["ingredients"]["coffee"]
    money += MENU[choice]["cost"]
    return f"Here is your {choice}. Enjoy!"


while not turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report()
    elif choice == "off":
        turn_off = True
    else:
        if check_resources(choice):
            user_money = insert_money()
            if user_money < MENU[choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                refund = round(user_money - MENU[choice]["cost"], 2)
                print(f"Here is ${refund} in change.")
                print(coffee_choice(choice))

