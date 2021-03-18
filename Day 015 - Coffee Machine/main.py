from data import MENU, resources

machine_on = True


def _report(res):
    print(f"water: {res['water']}ml\nmilk: {res['milk']}ml\ncoffee: {res['coffee']}g")


def _can_make(coffee, res):
    can_make = True
    for ingredient in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][ingredient] > res[ingredient]:
            can_make = False
    return can_make


def _get_coins(coffee):
    money_needed = MENU[coffee]["cost"]
    money_have = 0

    while money_needed > money_have:
        print(f"please insert ${money_needed - money_have}")
        get_quarters = int(input("How many quarters?: "))
        get_dimes = int(input("How many dimes?: "))
        get_nickles = int(input("How many nickles?: "))
        get_pennies = int(input("How many pennies?: "))

        money_have += (get_quarters * 25 + get_dimes * 10 + get_nickles * 5 + get_pennies) / 100

    if money_have > money_needed:
        change = money_have - money_needed
        print(f"Here is your change: {change}")

    return True


def _make_coffee(coffee, res):
    for ingredient in MENU[coffee]["ingredients"]:
        res[ingredient] -= MENU[coffee]["ingredients"][ingredient]
    print(f"Making {coffee}")
    print(".")
    print("..")
    print("...")
    print(f"Done! Enjoy your {coffee} 🤩")
    return res


while machine_on:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if _can_make(user_coffee, resources):
        if _get_coins(user_coffee):
            resources = _make_coffee(user_coffee, resources)
    else:
        print("Sorry, the machine is out of resources 🙃")
        machine_on = False

    if machine_on:
        should_continue = input("Would you like another coffee? 'y' or 'n': ")

        if should_continue == "n":
            print_report = input("Do you want to print a current report? 'y' or 'n': ")
            if print_report == 'y':
                _report(resources)
            else:
                machine_on = False




