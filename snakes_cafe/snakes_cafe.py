from textwrap import dedent

# on menu
menu_types = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Toranado",
              "A Litte Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]

# welcome message
welcome_message = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""

# Print it
print(welcome_message)

# make string
menu = """
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
"""

def main():
    # Define the greeting, menu, and closing messages
    greeting = "Welcome, what order can I get started for you?"
    menu = "We have wings, seafood, pasta, salad, and desserts. Type 'quit' to exit."
    closing = "Thank you, your order will be ready shortly."

    # Kim 411 on dictionary
    food_dict = {}

    print(greeting)
    print(menu)

    while True:
        food_selected = input("> ")
        if food_selected.lower() == "quit":
            break
        if food_selected in menu_types:
            # user info in dictionary increase count 1
            if food_selected in food_dict:
                food_dict[food_selected] += 1
                print(
                    f"** {food_dict[food_selected]} order of {food_selected} have been added to your meal **")
            # user info not in dictionary, add it with a count of 1
            else:
                food_dict[food_selected] = 1
                print(
                    f"** {food_dict[food_selected]} order of {food_selected} have been added to your meal **")

        else:
            print("I apologize we don't have that on our menu. Can I make a suggesttion?")

    # closing message
    print(closing)


if __name__ == "__main__":
    # Call the main function
    main()
