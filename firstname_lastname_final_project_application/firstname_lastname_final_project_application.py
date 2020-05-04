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

import firstname_lastname_final_project_utility as u #change the name of the file

def build_dict(filename):
    '''
    Creates an items_dict, k = product ID, v = [category, name, price, unit]
    items_dict populated from given input file contains all items
    Parameter: filename: string
    Returns: grocery_items_dict: dict
    '''
    items_dict = {}
    k = []
    v = []
    with open(filename, "r") as file:
        for line in file:
            data = line.split("|")
            key, value = data[0], data[1:]
            items_dict[key] = value
        return items_dict



def main():
    print('\n\n********** Welcome to InstantCart *************')
    grocery_items = build_dict('grocery_list_final.txt') #creates dict from the given input file
    cart = {} #dict to hold the customer items to purchase
    option = 0
    while option!=5:
        print("\n\tMain Menu\n\n\t1. Shop by category\n\t2. Shop by keyword\n\t3. Edit cart\n\t4. Checkout\n\t5. Exit Application\n")
        #display welcome message see sample I/O
        option = int(input('Enter option (1-5): '))
        if option == 1:
            u.shop_by_category(grocery_items, cart) #function in utiltiy file
        #your code here - user menu
        elif option == 2:
            u.shop_by_keyword(grocery_items,cart)
            #call appropriate function from the utility file
        elif option == 3:
            u.edit_cart(cart)
        elif option == 4:
            u.checkout(cart)
        elif option == 5:
            print("\n********* Thanks for using InstantCart ************")

if __name__== '__main__':
     main()
