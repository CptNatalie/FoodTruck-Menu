# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

menu_items = {}
order_list = []
# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")
# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    # Create a variable for the menu item number
    i = 1  
    # Create a dictionary to store the menu for later retrieval
    menu_items = menu.copy()
    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
    # Get the customer's input
    menu_category = input("Type menu number: ")
    
    # Check if the customer's input is a number
    if menu_category.isdigit():
        menu_category = int(menu_category)
        # Check if the customer's input is a valid option
        if menu_category in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(f"{key} + {key2}") 
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": f"{key} - {key2}",
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number (standdard input)
            menu_item_number = input("Enter the number of the item you'd like to order: ")

            # 3. Check if the customer typed a number (isdigit())
            if menu_item_number.isdigit():
             
                # Convert the menu selection to an integer int()
                menu_item_number = int(menu_item_number)

                # 4. Check if the menu selection is in the menu items look at the "keys()"
                if menu_item_number in menu_items.keys():
                    
                    # Store the item name as a variable (How do you get an item from a dictionary?(day3 04))
                  
                    item_name = menu_items[menu_item_number]["Item name"]


                    # Ask the customer for the quantity of the menu item (input?)
                    item_quantity  = input(f"How many {item_name} would you like to order? ")

                    # Check if the quantity is a number, default to 1 if not(if isdigit())
                    if item_quantity.isdigit():
                        item_quantity = int(item_quantity)
                    else:
                        item_quantity = 1    

                        # Add the item name, price, and quantity to the order list (append())
                  
                    order_list.append({
                            "Item name": item_name,
                            "Price": menu_items[menu_item_number]["Price"],
                            "Quantity": item_quantity
                            })

                        # Tell the customer that their input isn't valid
            else: 
                print("The information you entered is not valid")            


                #   Tell the customer they didn't select a menu option
                print("you didn't select an item on our menu.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")


        # Ask the customer if they would like to order anything else

    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's (use match/case here  Day3 activity 02and 3)

    if keep_ordering.upper() == "N":
        place_order = False
                               
                # Keep ordering

                # Exit the keep ordering question loop

    elif keep_ordering.upper() != "Y" and keep_ordering.upper() != "N":
            print("Invalid entery, please try again.")        
                # Complete the order
                 print("Your order is placed. We will call you when it is ready.")
                # Since the customer decided to stop ordering, thank them for
                # their order
                print(Thank you for dining with us!)
                # Exit the keep ordering question loop

                # Tell the customer to try again
        

# Print out the customer's order
print("This is what we are preparing for you.")
for item in order_list:
    print(f"Item: {order_list[0]['Item name']} - Quantity: {order_list[0]['Quantity']} - Price: ${order_list[0]['Price']}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
item_costs = [item_prices[i] * item_quantities[i] for i in range(len(order_list))]
total_cost = sum(item_costs)
print(f"The total price of your order is: ${total_cost:.2f}")