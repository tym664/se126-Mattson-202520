# Tyler Mattson
#
# Varubles used:
#
# price            Total Cost for item 
# tender           Amount Paid for item
# change           Change for transaction
# any_more_data    Any more data to be entered
# tax_rate         Tax Rate
# items            Number of items bought
# taxable_amount   Total tax
# is_taxed         Is there tax on items
# total_due        Total amount due
# total_cost       Total cost of items
# tot_tax_amnt     Total Tax Amount
###########################################################################
total_cost = 0.0
tot_tax_amnt = 0.0
tax_rate = 0.07
change = 0
price = 0
tender = 0
items = 0
taxable_amount = 0.0 
any_more_data = "y"





while any_more_data == "y":
    price = float(input("Total cost of purchase? : $"))
    items = items + 1
    total_cost += price
    is_taxed = input("Is the item taxable? (y/n)")
    if is_taxed == 'y':
        taxable_amount = price * tax_rate
        tot_tax_amnt += taxable_amount
        
    any_more_data = str(input("Do you want to contiune? [y/n]: ")).lower()

print()    
        
print ("-----------------In cart-----------------")
print ("You have " ,items,"items(s) in your cart")
print (f"Total cost of items: ${total_cost:9.2f}")
print (f"Total tax for items: ${tot_tax_amnt:9.2f}")
total_due = total_cost+taxable_amount
print (f"Total due:           ${total_due:9.2f}")
print ()


tender=float(input("How much money will be given to the clerk? $"))

if tender < total_due:
       print("Amount tendered is less than total due.")
       print("!---Invalid input---!.")
if tender > total_due:
       
       change = tender-total_due

print()
print ("--------------Reciept----------------")
print(f"Your change is:  ${change:4.2f}")
print ("-------------------------------------")
print()
print("Thank you for stopping at Stop N Shop")
print ()
print("--------------------------------------")
print ("Program has ended") 


