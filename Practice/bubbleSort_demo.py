#WEEK 8 DAY 1: BUBBLE SORT DEMO

#Binary Search can only be performed on ORDERED LISTS
#Lists can be ordered numerically or alphabetically
#       increasing (ascending) or decreasing (descending)

#FUNCTIONS-----------------------------------------------

def swap(listName, index):

    #this function handles the swapping of values for bubble sort
    temp_var = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp_var

    #processor has access to the new sorted list so we do not need to return specific list value -- it is already updated and we can access in main/base program code


#BASE (MAIN) PROGRAM-------------------------------------


name = ["Mary", "Cathy", "Tom", "Whitney", "Adam", "Sam", "Betty", "Ed"]

age = [21,33,24,28,30,31,40,68]

records = len(name) #len() returns the length of the list passed to it

print("BEFORE SORTING---------------------------------------------")
for i in range(0, records):

    print("INDEX: {0} \t {1:10} \t {2}".format(i, name[i], age[i]))


#BUBBLE SORT----------------------------------------------------------
for i in range(0, records - 1): #outter loop

    print("OUTTER LOOP! i = ", i) #not necessary for algorithm

    for k in range(0, records - 1): #inner loop

        print("\tINNER! k = ", k)
        
        #below if statement determines the sort
        #list used is the list being sorted
        #> is for increasing order, < is for decreasing order

        if name[k] > name[k + 1]:
            #first list value is greater than second list value; if putting in increasing order, they need to SWAP places

            print("\t\tSWAP! ", name[k], "<---->", name[k + 1])

            #swap the values
            #temp = name[k]          #
            #name[k] = name[k + 1]
            #name[k + 1] = temp
            
            swap(name, k)

            #swap the remaining values of the full record
            #this keeps all "original" data together -- stuff that belongs together
            #temp = age[k]
            #age[k] = age[k + 1]
            #age[k + 1] = temp

            swap(age, k)


print("\nEnd of Bubble Sorting \n\n\n")
print("ORDERED BY NAME---INCREASING, ALPHA-----------------------------")

for i in range(0, records):

    print("INDEX: {0} \t {1:10} \t {2}".format(i, name[i], age[i]))


#now that the NAMES are in increasing order, you would run a binary search for a NAME
