# Tyler Mattson
#
# Varubles used:
#  emp_name        Employee Name
#  hr_w            Hours Worked 
#  hr_r            Hourly Rate 
#  gp              Gross Pay
#  tot_gross       Total Gross Pay 
#  tot_tax         Total Tax
#  tot_net         Total Net Pay
#  tot_emp         Total Employees 
#  tax_rate        Tax Rate   
#  any_more_data   Any More Data 
############################################################################
tot_gross = 0
tot_tax = 0
tot_net = 0
tot_emp = 0
tax_rate = 0.20
any_more_data = "y"



while any_more_data == "y" :
        emp_name = (str(input("Enter Employees name")))
        print ()
        hr_w = (float(input("Enter hours worked ")))
        print()
        hr_r = (float(input("Enter hourly rate")))
        print ()
        
        gp = hr_w * hr_r
        tax = gp * tax_rate
        tot_tax = gp * tax_rate
        net = gp - tax
        
        tot_net = tot_net + net
        tot_gross = tot_gross + gp 
        print (f"Gross Pay {gp:8.2f}") 
        print (f"Total Tax {tot_tax:8.2f}")
        print (f"Total Net {tot_net:8.2f}")
        

        
        any_more_data = input("Any more Employees? [y/n]")
       
print (f"Total Net   {tot_gross:8.2f}")
print ()
print (f"Total Tax   {tot_tax:8.2f}")
print ()
print (f"Total Gross {tot_net:8.2f}")

