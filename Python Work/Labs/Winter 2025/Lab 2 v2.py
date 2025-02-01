#Tyler Mattson 
#Lab 2 Text file handing lab 
#Section: SE126 - 202502 (Morning Class) 
#Date: January 15 2024

#Thank you for helping me Katie. You're the best! 

#VARIABLE DICTIONARY---------
#computer_type = Desktop or Laptop
#maufacture = Dell or HP
#processor_type = i5 or i7
#ram = 8 or 16 GB
#hard_drive_size = How big the hard drive is
#num_HDD = Hard Drive 1
#second_drive_size = Hard Drive 2
#os = Operating System
#purchase_year = Year machine was purchased
       
#BASE PROGRAM CODE--------------------------------


#Importing csv libary 
import csv
totalRecords = 0

#Opening CSV file 
with open("filehandling.csv") as csvfile:

    file = csv.reader(csvfile)
    
#Headers for data placement     
    print("IT inventory:")
    print()
    print("=" * 130)
    print(f"{'Type':<10} {'Manufacturer':<15} {'Processor':<15} {'RAM(GB)':<10} {'HDD1'} \t{'Num HDD':>10} {'HDD2':>18} {'OS':>11.9} {'Purchase Year':>22}")
    print("-" * 130)

#For loop for handling data in the csv file
    
    for record in file:
        totalRecords += 1

#Conditional Statements for determing machine type and manufacturer
        if record[0] == 'D':
            computer_type = "Desktop"
        else:
            computer_type = "Laptop"

        if record[1] == 'DL':
            manufacturer = "Dell"
        elif record[1] == 'HP':
            manufacturer =  "HP"
        else:
            manufacturer =  "Gateway"

            
        processor_type = record[2]
        ram = record[3]
        hard_drive_size = record[4]
        num_HDD = int(record[5])

#Conditional statements for machines that have one or two HDD
        if num_HDD == 1:
            second_drive_size = "----"
            os = record[6]
            purchase_year = record[7]

        elif num_HDD == 2:
            second_drive_size = record[6]
            os = record[7]
            purchase_year = record[8]
            
        print(f"{computer_type:<10} {manufacturer:<15} {processor_type:>5} {ram:>15} {hard_drive_size:>10} {num_HDD:>12} {second_drive_size:>21} {os:>12} {purchase_year:>15}")
print("-" * 130)
print() 
print(f"\t\t\t\t\t\tTotal machines in file: {totalRecords}")
print()
print("-" * 130)
        

    
            
           
            
        

         
        
        
            


        
           
                

         

    
       
    
    
    
    
    
            

