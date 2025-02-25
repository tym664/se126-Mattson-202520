#W8D1 Intro to Dictionaries 
#start by creating a populated dictionary 

myCar = {
    #'key' : 'value',

    "make": "Lexus", 
    "model": "ES300",
    "year": 2000, 
    "name": " -- ",
    "color": "Gold",

#keys cannot be repeated, no dups allowed in dictionary
#repeats will replace first value added to the dictonary 

} 

#display entire dictonary 

print(myCar)

#display just the 'make' and 'model' values of the dictonary 

print(f"My car is a {myCar['make']} {myCar['model']}") 

#dictonaryName ['keyName'] --> accesses stored value 
#keyname will always be a STRING index, created by the developer 

yourCar = {
    #'key' : 'value',

    "make": "GMC", 
    "model": "Canyon",
    "year": 2019, 
    "name": "Jolly",
    "color": "black",
    "friends": ["Chevy", "Toyota", "Cadillac"]
    

#keys cannot be repeated, no dups allowed in dictionary
#repeats will replace first value added to the dictonary 

} 

print(f"Robs car is a {yourCar['make']} {yourCar['model']}") 

 #since "friends" gives access to a list, secondary [] are used to point which value in said list 
 
print(f"{yourCar["friends"][2]}") 

#processing through dictonary and its keys

for key in yourCar: 
    print(f"{key.upper()} : {yourCar[key]}") 

for key in myCar: 
    print(f"{key.upper()} : {myCar[key]}") 

#add a key and value to pre-existing dictionary 

yourCar ["plate"] = '12345' 