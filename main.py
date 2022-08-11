from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating objects and tied a class
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)
