import os

global price
price = []
sum(price)
global checkout_list
checkout_list = []





def build_dict_by_id(items):
    with open(items, "r") as file:
        check = input("Please input item ID or type any key to return:")
        check1 = check.upper()
        global p
        for line in file:
            currentline = line.split(",")
            for i in range(len(currentline)):
                if check1 == currentline[0]:
                    p = float(currentline[3])
                    price.append(p)
                    checkout_list.append(currentline)
                    break


def build_dict_by_category(items):
    tf = True
    while tf:
        with open(items, "r") as file:
            global check
            print("Welcome to shopping at Amazing!")
            print("We sell items in the following categories: ['book','cloth','elect','food']")
            check = input("Please input a category name or input 'checkout' to quit:")
            global item_id
            item_id = []
            information = []
            for line in file:
                currentline = line.split(",")
                if check == currentline[1]:
                    item_id.append(currentline[0])
                    inf = []
                    inf.append(currentline[1])
                    inf.append(currentline[2])
                    inf.append(currentline[3])
                    information.append(inf)


                elif check == "checkout":
                    tf = False

                    checkout(str(sum(price)))
                    print("reciept is ready..!!", sum(price))
                    break

            for i in range(len(item_id)):
                print("Item ID:", item_id[i], "\t\tInformation:", information[i])
            if tf == True:
                build_dict_by_id("items.txt")



def checkout(cart):
    with open("receipt.txt", "w+") as r:
        r.write("Thanks for shopping at Amazing.\n\nYou purchased the following item(s)\n\n")
        l4 = '\n'.join(','.join(sub) for sub in checkout_list)
        r.write(l4)
        r.write("\n**************************\n\nThe amount is: $")
        r.write(cart)
        r.close()


# build_dict_by_category("items.txt")
