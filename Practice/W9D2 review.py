#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(j, listName): 
    temp = listName[j]
    listName = [j] = listName [j + 1]
    listName[j + 1] = temp


#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)       #entire list
print(names_list[0])    #first value  
print(names_list[len(names_list) -1 ]) #Another way to provide the last index 


#Empty lists for storing data 
#These lists must remain that same length 
names = [] 
riders = [] 
nums = [] 
color1 = [] 
color2 = []

#creation & population of dictionaries
people_dictionary ={ 
    #"key" : value. Cannot duplicate keys in dictionary 
    "fname" : "George",
    "mname" : "Bulleit",
    "lname" : "Wayne",
    "age" : 12, 
    "age" : 12.5,
}

print(people_dictionary)#Prints entire dictionary 
print(people_dictionary["fname"])#Prints the value assinged at key position.(Will bring fname as well as George)

dragons_dict = {} #Empty dictionary for populating data 


#gaining data from a text file 
with open("text files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        print() #we will replace this during demo

        #adding data to a list 


        #adding data to a dictionary
        names.append = [rec[0]] 
        riders.append = [rec[1]] 
        nums.append = [rec[2]] 
        color1 = [rec[3]]

        if rec[2] == "2": 
            color2.append (rec[4])
        else: 
            color2.append("None") #Error check


#processing data from collections
print(f"{'NAMES':12} {'RIDERS' :20} {'NUM' :3} {'COLOR1' :8} {'COLOR2'}") #Headers 
print("=" * 50)#Formatting 
for i in range(0, len(names)): #Index will run from 0 all the way to names 
    print(f"{names[i]:12} {riders[i]:20} {nums[i]:3} {color1[i]:8} {color2[i]}")#Printing index to user 
print("=" * 75)#Formatting 



#searching & sorting
for key in dragons_dict: 
    if search.lower() in dragon_dict[key][0]: 



#2D lists - lists of lists! 