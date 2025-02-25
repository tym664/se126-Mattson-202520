#W8D2 Dictonarys and text file data 

import csv 

library = { 
    #indexes are strings set by the developer
    #'key' : 'value' pair 
    "1230" : "Red Rising", 
    "1231" : "The Little Prince",

}



with open("text files/dictionary_file.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file:

        library.update({rec[0] : rec[1]}) 

#Diconnect from file 
print()
print(f"{'KEY':>6}\t{'TITLE':>8}") 
print("=" * 35)
print()

for key in library: 

    print(f"{key:>6}\t{library[key]}") 
print()    
print("=" * 35) 

#Sequential Searchig for a title 

search = input("Enter the title you are looking for: ")
print()

found = 0 

for key in library: 
    if search.lower() == library[key].lower(): 

        found = key

if found != 0: 

    print(f"KEY:{found}\tTITLE:{library[found]:8}") 

else: 
    print(f"Your search for {search} was not found") 





        
        
