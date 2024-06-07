from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coin_operator = MoneyMachine()
my_coffee_maker = CoffeeMaker()


# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def prompt_user():
    # TODO: 1b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
    #  The prompt should show again to serve the next customer.
    while True:
        # TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
        user_input = input(f" What would you like? ({my_menu.get_items()}): ").lower()
        # TODO: 1a. Check the user’s input to decide what to do next.
        # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
        if user_input == 'off':
            print("Turning coffee machine off.")
            exit()
        # TODO: 3. Print report
        elif user_input == 'report':
            my_coffee_maker.report()
            my_coin_operator.report()
        elif my_menu.find_drink(user_input):
            drink = my_menu.find_drink(user_input)
            cost = drink.cost
            if my_coffee_maker.is_resource_sufficient(drink):
                # TODO: 5. Process coins.
                # TODO: 6. Check transaction successful?
                if my_coin_operator.make_payment(cost):
                    # TODO: 7. Make Coffee
                    my_coffee_maker.make_coffee(drink)
        else:
            print("Incorrect input! Type 'espresso' or 'latte' or 'cappuccino'")
            continue


def main():
    prompt_user()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
