
#Tyler Mattson
# not_eligible = Not eligible to note
#not_registed_but_eligible = Not registed but eligible to vote
#eligible_not_voted = eligible but did not vote
#tot_voted = total voted
#more_data = any more data to input
#id_number = ID number
#age = age
#number_ran = number of times records were processed
#tot_nonvote = total not voted
#tot_young = total that are too young
#tot_invid = total invalid IDs
##############################################################################################################################
not_eligible = 0
not_registered_but_eligible = 0
eligible_notvoted = 0
tot_voted = 0
more_data = "y"
id_number = 0
age = 0
number_ran = 0
tot_nonvote = 0
tot_young = 0
tot_invid = 0
tot_noneligible = 0 

while more_data == "y":
    
    id_number = input("Enter ID number")
    
    if len(id_number)==4:
        
        id_number = int(id_number)
        age = int(input("Enter age"))
        
        if age >= 18:
            
            eligible_not_voted = input("Are you eligible to vote?(Y/N)").lower()
            
            
            if eligible_not_voted =="y":
                eligible_notvoted =+1
                voted = input("Did you vote?")
                
                if voted == "y":
                    tot_voted += 1

              
                    print()
                else:
                    print("User did not vote")
                    tot_nonvote +=1
                    
                     

            else:
                
                print ("Not eligible")
                tot_noneligible +=1
                not_registered_but_eligible +=1
        
        else:
            
            print ("Too young")
            tot_young +=1 

    else:
        
        print("Invalid ID number")
        tot_invid +=1
        
    number_ran += 1
    more_data = input("Do you have more data to enter? (Y/N): ").lower()
    
print("\nAnalysis Results:")
print ("-------------------")
print(f"1. Number of individuals not eligible to register: {tot_noneligible}")
print()
print(f"2. Number of individuals who are old enough to vote but have not registered: {tot_young}")
print()
print(f"3. Number of individuals who are eligible to vote but did not vote: {eligible_notvoted}")
print()
print(f"4. Number of individuals who did vote: {tot_voted}")
print ()
print(f"5. Number of records processed: {number_ran}")
print ()
print (f"6. Number of invalid IDs: {tot_invid}")
