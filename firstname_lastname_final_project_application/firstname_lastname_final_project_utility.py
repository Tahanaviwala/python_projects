#-------------------------------------------------------------------------------
# Student Name: 
# Assignment: Final Project
# Python version:
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation
#-------------------------------------------------------------------------------
# Notes: Any general comments to the grader
#-------------------------------------------------------------------------------

import random, string

def add_to_cart(all_items, cart):
    '''
    Add an item to cart dictionary
    Parameter: all_items, cart: dict
    Returns: None
    '''
    print("\nAdd to cart")
    product_id = str(input("Enter item ID as it appears:"))
    quantity = str(input("Enter quantity of item:"))
    #create a key-value pair in the cart dict
    all_item = []
    for i in all_items:
        if product_id in i[0]:
            all_item.append(i[1])
    value = listToString(all_item)
    cart[product_id] = "   " + value.strip() + "    " + quantity
    #key = product id, value = [category, name, price, unit, quantity]
    #quantity represents how many user wants
    #append quantity to the end of the value list

def display_cart(cart):
    '''
    Display current cart items -> see sample I/O
    Parameter: cart: dict
    Return: None
    '''
    print("\n******** Your current cart ***********\n ID    name     category     price     unit     quantity\n")
    for i in cart:
        print(i, cart[i])
    #display key and values


#option - 2
def shop_by_keyword(all_items, cart):
    '''
    Allow user to purchase item by keyword
    as long as user wants to continue
    Parameter: all_items , cart: dict
    Returns: None
    '''
    choice = 'y'
    while choice == 'y':
        keyword = input('\nEnter your keyword (Example: egg, milk): ')
        #your code here
        #iterate over all_items dictionary
        available_value = []
        available_key = []
        for key, value in all_items.items():
            if keyword in value[0] or keyword.title() in value[0]:
                available_value.append(value)
                available_key.append(key)

        item_list = []
        for i in range(len(available_key)):
            print(available_key[i] + "   ", listToString(available_value[i]), end="")
            item_list.append([available_key[i], listToString(available_value[i])])

        #call add_to_cart -> user add an item
        add_to_cart(item_list, cart)
        display_cart(cart)
        #call display_cart -> display cart
        #ask for choice
        choice = input('\nDo you continue adding (y/n): ')


        
#option - 1       
def shop_by_category(all_items, cart):
    '''
    Allow user to purchase item by category
    as long as user wants to continue 
    Parameter: all_items , cart: dict
    Returns: None
    '''
    print("\nAvailable Categories:")
    ava_cat = []
    # all_item = all_items.values()
    for i in range(len(all_items)):
        ava_cat.append(all_items["ID"+str(i+1)][1]+" ")
    list_ava = list(set(ava_cat))
    available = ", ".join(list_ava)
    print(available)
    c_name = str(input("\nEnter category name:"))
    available_value = []
    available_key = []
    for key, value in all_items.items():
        if c_name in value:
            available_value.append(value)
            available_key.append(key)
    item_list = []
    for i in range(len(available_key)):
        print(available_key[i] + "   ", listToString(available_value[i]) , end="")
        item_list.append([available_key[i] , listToString(available_value[i])])

    choice = 'y'
    while choice == 'y':
        add_to_cart(item_list,cart)
        display_cart(cart)
        choice = str(input("\nDo you continue adding(y/n:)"))

#option - 3       
def edit_cart(cart):
    '''
    Edit cart with change quantity or delete an item
    Parameter: cart: dict
    Return: None
    '''
    menu = '\n1. Change Quantity\n2. Delete item\n'
    print(menu)
    choice = int(input('Enter option to edit cart (1-3): '))
    #your code here
    if choice == 1:
        display_cart(cart)
        #your code here
        #ask for product ID and quantity to change
        product_id = str(input("\nEnter item ID as it appears:"))
        quantity = str(input("Enter quantity of item:"))
        get_value = cart.get(product_id)
        value_to_list = list(get_value.split("    "))
        value_to_list[-1] = quantity
        values = listToString(value_to_list)
        cart[product_id] = values
        display_cart(cart)
        # create a key-value pair in the cart dict
        print("Cart Updated..!!")

    elif choice == 2:
        display_cart(cart)
        #ask for product ID
        product_id = str(input("\nEnter item ID as it appears:"))
        #delete the item by product ID
        if product_id in cart:
            del cart[product_id]
        display_cart(cart)
        print("\nCart Updated..!!")
    else:
        print('Return to main menu')


# def subtotal(cart):
#     '''
#     Calculates subtotal of the cart
#     Parameter: cart: dict
#     Return: sub total of all the cart items: float
#     '''
#     #your code here
#
def get_receipt_number():
    return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))
#
#option - 4
def checkout(cart):
    '''
    Display Check out information for a user
    Paramter: cart: dict
    Retunr: None
    '''
    #your code here

    #display receipt number, cart items, subtotal
    print("*********** Your Receipt ***********")
    print("\t\tReceipt No."+get_receipt_number())
    print(display_cart(cart))
    print("************************************\n")
    value = list(cart.values())
    quantities = []
    price = []
    for i in value:
        value_to_list = list(i.split("    "))
        quantities.append(int(value_to_list[4]))
        price.append(float(value_to_list[2]))
    sub_total = []
    for i in range(len(quantities)):
        sub_total.append(quantities[i] * price[i])
    subtotal = sum(sub_total)
    print("Your subtotal: " + str(subtotal))
    tax = (subtotal*4.3)/100
    print("Your tax: " + str(f"{tax:.2f}"))
    total = subtotal-tax
    print("Your Total: " + str(f"{total:.2f}"))
    print("************************************")


        #calculate and display tax 4.3%
    #display total
#     #see sample I/O for format
    
def listToString(s):
    str1 = "     "
    return (str1.join(s))