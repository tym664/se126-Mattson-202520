#Katie Truchon
#Practice 1B SOLUTION FILE [Lab#]
#Date: July 22 2020

#* comments are lines that were suggested to change from Practice 1A in order to complete Practice 1B

#VARIABLE DICTIONARY---------
#sumtotalTemps          the sum total of all F temps entered during session
#totalGTemps            the number of temps entered during session

#FUNCTIONS------------------------------------------

#BASE PROGRAM CODE--------------------------------

#initialize variables
sumtotalTemps = 0
totalTemps = 0

print("Welcome to my Fahrenheit-to-Celsius Conversion Program")

#answer = input("Enter y to start: ")
num_temps = int(input("Enter how many temperatures you would like to convert today: "))

while totalTemps < num_temps:

    tempF = float(input("\tEnter tempF: "))

    tempC = (tempF - 32) * (5 / 9)

    #update sumtotal of all tempF values    
    sumtotalTemps += tempF 
    #same as: sumtotalTemps = sumtotalTemps + tempF

    totalTemps += 1
    #totalTemps = totalTemps + 1

    
    print("\tTOTAL TEMPS: ", totalTemps)
    print("\tTemp F is {0:.1f} = Temp C is {1:.1f}".format(tempF, tempC))

    #FOR TESTING --> print("current sum total: ", sumtotalTemps)

    #answer = input("\tWould you like to enter another temperature? [y/n]: ")

    #removes the case sensitiviy of char/string entered
    #answer = answer.lower()

    #check the user's value for answer (make sure it's y or n); trap user in a loop if not, until y/n is given 
    #while answer != "y" and answer != "n":
      #tell user they messed up
    #  print("**ERROR!**")

      #allow user to re-enter a value; gives possiblity of quitting the loop!
    #  answer = input("\tWould you like to enter another temperature? [y/n]: ")

      #removes the case sensitiviy of char/string entered
    #  answer = answer.lower()
      



#calculate average
avgTempF = sumtotalTemps / totalTemps

avgTempC = (avgTempF - 32) * (5 / 9)

print("\nTOTAL TEMPERATURES: ", totalTemps)
print("AVERAGE TEMPERATURE: {0:.1f}F | {1:.2f}C".format(avgTempF, avgTempC))

print("\n\nThank you. Goodbye")