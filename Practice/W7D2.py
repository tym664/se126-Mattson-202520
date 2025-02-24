
def menu(): 
    print()
    print("\t\t\t\t\t****Simple Search menu****")
    print() 
    print("\t\t\t\t\t1. Search by NAME")
    print("\t\t\t\t\t2. Search by NUM") 
    print("\t\t\t\t\t3. Search by COLOR") 
    print("\t\t\t\t\t4. EXIT")
    print()
    print ("=" * 115 )

    menuChoice = input("Enter your search type [1-4]:")
    return menuChoice


import csv  

#Empty 1D lists
names = []
nums = []
colors = [] 


validMenu = ["1", "2", "3" , "4"]

with open("text files/simple-2.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2].title())


ans = "y"

while ans == "y":
    choice = menu()

    if choice not in validMenu: 
        print("NOT A VALID INPUT")

    elif choice == "1":
        print("\t\t\t\tSearch by NAME:")

        min = 0 
        max = len(names) -1 
        mid = int((min + max) / 2)


        search = input("Enter the NAME")

        while min < max and search.lower() != names[mid].lower(): 
            if search.lower() < names[mid].lower(): 
                max = mid -1 
            else: 
                min = mid + 1 

            mid = int((min + max) / 2)
        if search.lower() == names[mid].lower(): 

            print(f"Search for {search} is complete: ")
            print (f"{'NAME' :8} {'NUM':3}  {'COLOR'}")
            print("=" * 115)
            print()
            print(f"{names[mid]:8} {nums[mid]:3}  {colors[mid]}")
            print()
            print("=" * 115)
        else: 
            print(f"Your search for {search} was not")


    elif choice == "2":
        print("\t\t\t\tSearch by NUM:")



    elif choice == "3":
        print("\t\t\t\tSearch by COLOR:")
        for i in range(len(colors)-1): 
            for j in range(len(colors)-1): 
                if colors[j] > colors [j + i]: 
                    
    else: 
        print("\t\t\t\tEXIT")
        print("\t\t\t\tPROGRAM HAS FINISHED, THANK YOU.") 


                                                