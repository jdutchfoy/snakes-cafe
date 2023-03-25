from textwrap import dedent

# menu_types = {
#     'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
#     'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
#     'Desserts': ['Ice Cream', 'Cake', 'Pie'],
#     'Drinks': ['Coffee', 'Tea', 'Unicorn Tears'],
# }

menu_types = ["Wings", "Cookies", "Spring Rolls","Salmon", "Steak","Meat Toranado", "A Litte Garden", "Ice Cream","Cake" , "Pie", "Coffee", "Tea", "Unicorn Tears" ]

welcome_message = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
print(welcome_message)

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

def main():
    print(dedent("""
# corrected string literal
print("***********************************")
print("** What would you like to order? **")
print("***********************************")

# for i in food_dict:
#     if food_selected == food_dict[i]:
#         food_dict[selected] += 1
#         print(f"** {food_dict[selected]} order of {food_selected} have been added to your meal **")

# if next_order == food_dict[i]:
#     food_dict[next_order] += 1
#     print(f"** {food_dict[next_order]} order of {next_order} have been added to your meal **")

# print(order_options)?
# def order_options(): ?
# format structure assisted from friend Dom James

food_dict = {}
greeting = "Welcome, what order can I get started for you?"
menu = "We have wings, seafood, pasta, salad, and desserts. Type 'quit' to exit."
closing = "Thank you, your order will be ready shortly."

def main():
    print(greeting)
    print(menu)

    while True:
        food_selected = input("> ")
        if food_selected.lower() == "quit":
            break

        if food_selected in food_dict:
            food_dict[food_selected] += 1
            print(f"** {food_dict[food_selected]} order of {food_selected} have been added to your meal **")
        else:
            print("I apologize we don't have that on our menu. Can I make a suggesttion.")

    print(closing)

if __name__ == "__main__":
    main()







