class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=150),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=100),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=200),
        ]

    def get_items(self):
        return "/".join([item.name for item in self.menu])

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None


class CoffeeMachine:
    def __init__(self):
        self.resource = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        print(f"Water: {self.resource['water']}ml")
        print(f"Milk: {self.resource['milk']}ml")
        print(f"Coffee: {self.resource['coffee']}g")

    def is_resource_suffcient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resource[item]:
                print(f"Sorry, there iis noto enough {item}")
                return False
        return True

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resource[item] -= order.ingredients[item]
        print(f"Here is you ☕ {order.name}. Enjoy!")


class MoneyMachine:
    CURRENCY = "Rs."

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY} {self.profit}")

    def make_payment(self, cost):
        money = int(input("How much money: "))
        if money >= cost:
            self.profit += cost
            print(f"Here is your change: {self.CURRENCY} {money - cost}")
            return True
        return False


menu = Menu()
coffee_maker = CoffeeMachine()
money_machine = MoneyMachine()

is_on = True
while is_on:
    print("\n---VIRTUAL CLI COFFREE MACHINE---")
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if len(choice) < 1 or not choice.isalpha():
        print("Invalid input! Try again.")
        continue

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if (
            drink
            and coffee_maker.is_resource_suffcient(drink)
            and money_machine.make_payment(drink.cost)
        ):
            coffee_maker.make_coffee(drink)
