# Tyler Mattson
#
# Varubles used:
#  hr_rate      Hourly Rate
#  hr_wrk       Hours Worked
#  tax_rate     Tax Rate
#  net_pay      Net Pay
#  gross_pay    Gross Pay 
###############################################################################
hr_rate = 14.50
hr_wrk = 32
tax_rate = .20
gross_pay=hr_rate*hr_wrk
tax=gross_pay*tax_rate
net_pay=gross_pay-tax
print(gross_pay)
print()
print(tax)
print(net_pay)


