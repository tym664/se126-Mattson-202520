#W6D2 - Bubble Sorting & Binary Search Review

#https://www.google.com/search?q=bubble+sort+visualization&rlz=1C1GCHA_enUS1119US1119&oq=bubble+sort+visualization&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIICAQQABgWGB4yCAgFEAAYFhgeMg0IBhAAGIYDGIAEGIoFMg0IBxAAGIYDGIAEGIoFMg0ICBAAGIYDGIAEGIoF0gEIMzUwMmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:7e94f359,vid:0BkoXZBbhfU,st:0 

#***IMPORTANT: 
#   In order to use binary search, 2 caveats must be fulfilled:
#      *the list we intend to search through is ORDERED
#      *the list we intend to search through is populated with UNIQUE VALUES (no repeats!)

#----IMPORTS-------------------------------------------------
import csv

#----FUNCTIONS-----------------------------------------------
def display(x, foundList, records):

    if x != "x":
        print(f"{class_type[x]:8} {name[x]:10} {meaning[x]:20} {culture[x]}")

    elif foundList: 
        for i in range(0, records): 
            print(f"{[class_type[i]]:8} {[name[i]]:10} {[meaning[i]]:20} {[culture[i]]}")

    else:
        for i in range(0, len()): 
            print(f"{class_type[i]:8} {name[i]:10} {meaning[i]:20} {culture[i]}")

def swap(i, listName): 
    temp = listName [i]
    listName[i] = listName [i + 1] 
    listName[i + 1] = temp 

#----MAIN CODE-----------------------------------------------
class_type = [] #rec[0] in file; repeats --> SEQUENTIAL
name = []       #rec[1] in file; unique  --> BINARY
meaning = []    #rec[2] in file; unique  --> BINARY
culture = []    #rec[3] in file; repeats --> SEQUENTIAL

with open("text files/party.csv", encoding="utf-8") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file: 
        print(rec)
        #rec is a 1D list and file is a 2D list
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])

#disconnect from file & test file connection + list storage
print(f"{'TYPE':8}   {'NAME':10}   {'CULTURE':10}   {'MEANING'}") #HEADER PRINT
print("-----------------------------------------------------------------------")
for i in range(0, len(class_type)):
    print(f"{class_type[i]:8}   {name[i]:10}   {culture[i]:10}   {meaning[i]}")
print("-----------------------------------------------------------------------\n")




#BINARY SEARCH: requires the list to be populated with unique values + be ORDERED
answer = "y"
search_type = 0
while answer.lower() == "y" and search_type != 4:

    print("\tMENU")
    print("\t1. Search by TYPE")
    print("\t2. Search by NAME")
    print("\t3. Search by MEANING")
    print("\t4. to EXIT")

    search_type = int(input("\nHow would you like to search today? [1-4]"))
    if search_type == 4:
        print("\n\nThank you for using my program, GOODBYE!\n\n\n")

    else: 
        #handles searching options
        if search_type == 1: #TYPE --> sequential search

            search = input("\nEnter the TYPE you are looking for [dragon/elf]: ")

            for i in range(0, len(class_type)):
                if search.lower() == class_type[i].lower():
                    print(f"{class_type[i]:8}   {name[i]:10}   {culture[i]:10}   {meaning[i]}")


        elif search_type == 2: #NAME --> binary 
            #BUBBLE SORT ALGORITHM
            for i in range(0, len(name) - 1):#outter loop
                #print("OUTER LOOP! i = ", i)

                for index in range(0, len(name) - 1):#inner loop
                    #print("\t INNER LOOP! k = ", index)

                    #below if statement determines the sort
                    #list used is the list being sorted
                    # > is for increasing order, < for decreasing

                    if(name[index] > name[index + 1]):
                        #print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

                        #if above is true, swap places!
                        temp = name[index]
                        name[index] = name[index + 1]
                        name[index + 1] = temp

                        #swap all other values
                        temp = class_type[index]
                        class_type[index] = class_type[index + 1]
                        class_type[index + 1] = temp

                        temp = culture[index]
                        culture[index] = culture[index + 1]
                        culture[index + 1] = temp

                        temp = meaning[index]
                        meaning[index] = meaning[index + 1]
                        meaning[index + 1] = temp
            print("\t\tORDERED BY *NAME*")
            print(f"{'TYPE':8}   {'NAME':10}   {'CULTURE':10}   {'MEANING'}") #HEADER PRINT
            print("-----------------------------------------------------------------------")
            for i in range(0, len(class_type)):
                print(f"{class_type[i]:8}   {name[i]:10}   {culture[i]:10}   {meaning[i]}")
            print("-----------------------------------------------------------------------\n")




            search = input("\nEnter the NAME you are looking for: ")

            #now that it is ordered by name, we can now perform BINARY SEARCH
            min = 0 
            max = len(name) - 1
            mid = int((min + max)/2)

            while min < max and search != name[mid]:
                if search < name[mid]:
                    max = mid - 1
                else:
                    #search > name[mid]
                    min = mid + 1
                mid = int((min + max)/2)

            if search == name[mid]:
                print(f"We FOUND {search} !")
                print(f"{class_type[mid]:8}   {name[mid]:10}   {culture[mid]:10}   {meaning[mid]}")
            else:
                print(f"We DID NOT FIND {search} :[")

        elif search_type == 3: #MEANING
            word = input("Which MEANING KEYWORD are you looking for? ")

            #run sequential search to view ALL meaning values
            for i in range(0, len(meaning)):

                #check to see if word is IN meaniing:
                if word.lower() in meaning[i].lower():
                    print(f"{class_type[i]:8}   {name[i]:10}   {culture[i]:10}   {meaning[i]}")

        else:
            print("\n\nSorry, that option is not recognized. Please try again.")
    


    answer = input("\nWould you like to search again? [y/n]")