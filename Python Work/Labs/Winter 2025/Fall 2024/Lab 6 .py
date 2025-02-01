
#Tyler Mattson
#any_more = Any more data 
#na1 = Number 1 for adding 
#na2 = Number 2 for adding 
#ns1 = Number 1 for subtracting
#ns2 = Number 2 for subtracting
#nd1 = Number 1 for dividing
#nd2 = Number 2 for dividing
#nm1 = Number 1 for multiplication
#nm2 = Number 2 for multiplication
#choice = User input for desired function 
##############################################################################################################################
any_more = "y"

# Function for addition
def add(na1, na2):
    return na1 + na2

# Function for subtraction
def subtract(ns1, ns2):
    return ns1 - ns2


# Function for division
def divide(nd1, nd2):
    if nd1 == 0:
        return "Undefined"
    elif nd2 == 0:
        return "Undefined"
    return nd1 / nd2

# Function for multiplication   
def multiply(nm1,nm2):
    return nm1 * nm2
    

while any_more == "y" :
        print ()
        print("Welcome to Tylers Calculator. Select an operation:")
        print("--------------------------------------------------")
        print()
        print ("\t\t|=============|")
        print("\t\t|1. Add       |")
        print("\t\t|2. Subtract  |")
        print("\t\t|3. Divide    |") 
        print("\t\t|4. Multiply  |")
        print("\t\t|5. Exit      |")
        print("\t\t|=============|")
        print()
        choice = input("Enter desired function (1, 2, 3, 4 or 5): ")
        print()
        
        if choice == '1':
                na1 = float(input("Enter first number to be added: "))
                print("====================================")
                na2 = float(input("Enter second number to be added: "))
                print ("===================================")
                print (f" {na1} + {na2} = {add(na1, na2)}")
                print("====================================")

        elif choice == '2':
                ns1 = float(input("Enter first number to be subtracted: "))
                print("====================================")
                ns2 = float(input("Enter second number to be subtracted: "))
                print("====================================")
                print (f"{ns1} - {ns2} = {subtract(ns1, ns2)}")
                print("====================================")

        elif choice == '3':
                nd1 = float(input("Enter first number to be divided: "))
                print("====================================")
                nd2 = float(input("Enter second number to be divided: "))
                print("====================================")
                print (f" {nd1} / {nd2} = {divide(nd1, nd2)}")
                print("====================================")


        elif choice == '4':
                nm1 = float(input("Enter first number to be multiplied: "))
                print("====================================")
                nm2 = float(input("Enter second number to be multiplied: "))
                print("====================================")
                print (f" {nm1} * {nm2} = {multiply(nm1, nm2)}")
                print("====================================")
                

        elif choice == '5':
            print ("Exiting program. Thank you")
            break

        else:
            print ("!!Invalid Input. Please choose 1, 2, 3, 4 or 5!!")
            print ()
            

        
     
           

        

        

       
            
                


                
                


                
                
        

    

        

    



    
       
