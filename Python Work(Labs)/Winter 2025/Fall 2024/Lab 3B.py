# Tyler Mattson
#
# Varubles used:
#
# price            Total Cost for item 
# tender           Amount Paid for item
# change           Change for transaction
# any_more_data    Any more data to be entered          
############################################################################
amount_paid = 0
total_cost = 0
change = 0
price = 0
tender = 0
items = 0 
any_more_data = "y"



while any_more_data == "y":
    price = float(input("Total cost of purchase? : $"))
    total_cost = total_cost + price
    items = items + 1
    any_more_data = str(input("Do you want to contiune? [y/n]"))  
print ()
print ("You have " ,items,"items(s) in your cart")
print (f" Your total cost is ${total_cost:3.2f}")
print()
tender = float(input("How much money will be given to the clerk? $"))
change = tender-total_cost
print()
print(f"  Your change is ${change:3.2f}")
print()
print("Have a nice day")
       


