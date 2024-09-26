import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            print("Turning off the machine.")
            break
        elif choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif choice in ["small", "medium", "large"]:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            # Check if resources are sufficient
            if sandwich_maker_instance.check_resources(ingredients):
                # Process coins and complete transaction
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
                    print(f"{choice} sandwich is ready. Bon appetit!")
        else:
            print("Invalid option. Please try again.")

if __name__=="__main__":
    main()