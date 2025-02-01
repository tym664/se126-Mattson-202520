#Tyler Mattson 
#Lab 1  PROGRAM THAT DETERMINES IF A ROOM IS IN VIOLATION OF FIRE REGULATIONS
#Section: SE126 - 202502 (Morning Class) 
#Date: January 12 2024


#VARIABLE DICTIONARY---------
#additionalPeople -> Amount of additional people that can be added to the room
#peopleToExclude -> Amount of people that need to be removed from the room
#maxCap -> Maximun amount of people that can be in the room
#attendees -> Amount of people attending the meeting
#response -> Variable for entering anymore data
#regulationCheck = Variable that checks the amount of people in a meeting against the function 
        
#BASE PROGRAM CODE--------------------------------

#VARIABLES
additionalPeople = 0 
peopleToExclude = 0
maxCap = 0
attendees = 0
resp = "y"

def descision (response):

    while response != "y" and response != "n":
        
        print("\t\t!****ERROR*****!")
        
        response = input ("\t\tWould you like to check another room? (y/n): ").lower()
        print()
        
    return response 

def difference (maxCap, attendees):
    diff = maxCap-attendees
    return  diff
    

print("\t\tWelcome to fire prevention saftey counsler")

print ("\t\t------------------------------------------")
print()
       
while resp == "y": 


        maxCap = int(input("\t\tEnter maximun room capacity"))
        print ("\t\t-----------------------------------------------------------")
        print()
        attendees = int(input("\t\tEnter amount of people attending the meeting"))
        print ("\t\t-----------------------------------------------------------")
        print()

        regulationCheck = difference(maxCap, attendees)
        
         

        if regulationCheck == 0:
            print () 
            print("The meeting can be held legally")

        elif regulationCheck < 0:
            print (f"\t\tThere are too many people attending the meeting. You need to remove {regulationCheck * -1} extra people")
            print("\t\t---------------------------------------------------------------------------------")
            print () 

        else: 
            print (f"\t\tThe meeting can be held legally. You can add {regulationCheck} amount of people in the meeting")
            print ("\t\t-----------------------------------------------------------------------------------")
            print()
             


        resp = input("\t\tWould you like to check another room? (y/n): ").lower()
        resp = descision(resp)
        print("\t\t///////////////////////////////////////////////////////////")
        print()

       
print ("\t\tExiting Program") 

            
                
            
           
            
        

         
        
        
            


        
           
                

         

    
       
    
    
    
    
    
            

