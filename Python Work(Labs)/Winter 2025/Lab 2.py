#Tyler Mattson 
#Lab 2 Text file handing lab 
#Section: SE126 - 202502 (Morning Class) 
#Date: January 15 2024


#VARIABLE DICTIONARY---------
#computer_type = Desktop or Laptop
#maufacture = Dell or HP
#processor_type = i5 or i7
#ram = 8 or 16 GB
#hard_drive_size = How big the hard drive is
#HDD1 = Hard Drive 1
#HDD2 = Hard Drive 2
#os = Operating System
#purchase_year = Year machine was purchased
       
#BASE PROGRAM CODE--------------------------------


import csv

totalRecords = 0



with open("filehandling.csv") as csvfile:

    file = csv.reader(csvfile)
    
    print("IT inventory:")
    print("=" * 150)
    print(f"{'Type':<10} {'Manufacturer':<15} {'Processor':<20} {'RAM (GB)':>5} {'HDD #'} \t{'HDD1':>15} {'HDD2':>18} {'OS':>11.9} {'Purchase Year':>15}")
    print("-" * 150)

    
    for record in file:
        totalRecords += 1
        records = [0]
        
        computer_type = "Desktop" if record[0] == 'D' else "Laptop"
        manufacturer = "\tDell" if record[1] == 'D' else "\tHP" if record[1] == 'HP' else "\tDell"
        processor_type = record[2]
        ram = record[3]
        hard_drive_size = record[4]
        HDD1 = int(record[5])
        HDD2 = int(record[5])


        if HDD1 == 1:
            HDD1 == record[6]
            os = record[6]
            purchase_year = record[7]
            print(f"{computer_type:<10} {manufacturer:<15} {processor_type:<20} {ram:<20}  {hard_drive_size} {HDD1:<20} {os:>10} {purchase_year:>10}")

        elif HDD2 == 2:
            HDD2 = record[6]
            os = record[7]
            purchase_year = record[8]
            print(f"{computer_type:<10} {manufacturer:<15} {processor_type:<20} {ram:<5} {HDD1} {HDD2:>38} {os:>12} {purchase_year:>10}")
                
print() 
print(f"\t\tTotal machines in file: {totalRecords}")
print("-" * 150)
        

    
            
           
            
        

         
        
        
            


        
           
                

         

    
       
    
    
    
    
    
            

