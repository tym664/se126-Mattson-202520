#Katie Truchon
#Practice 1C SOLUTION FILE [Lab#]
#Date: July 22 2020

#* comments are lines that were suggested to change from Practice 1A in order to complete Practice 1B

#VARIABLE DICTIONARY---------
#sumtotalTemps          the sum total of all F temps entered during session
#totalGTemps            the number of temps entered during session

#FUNCTIONS------------------------------------------
def converter(f):

  c = (f - 32) * (5 / 9)

  #the return value is returned exactly to the point of call of the function
  return c


def again():

  answer = input("\tWould you like to enter another temperature? [y/n]: ")

  #removes the case sensitiviy of char/string entered
  answer = answer.lower()

  #check the user's value for answer (make sure it's y or n); trap user in a loop if not, until y/n is given 
  while answer != "y" and answer != "n":
    #tell user they messed up
    print("**ERROR!**")

    #allow user to re-enter a value; gives possiblity of quitting the loop!
    answer = input("\tWould you like to enter another temperature? [y/n]: ")

    #removes the case sensitiviy of char/string entered
    answer = answer.lower()


  #after the loop check (making sure it's y/n) return value to the main program 
  return answer


#BASE PROGRAM CODE--------------------------------

#initialize variables
sumtotalTemps = 0
totalTemps = 0

print("Welcome to my Fahrenheit-to-Celsius Conversion Program")

ans = input("Enter y to start: ")
#num_temps = int(input("Enter how many temperatures you would like to convert today: "))

#while totalTemps < num_temps:
while ans == "y" or ans == "Y":

    tempF = float(input("\tEnter tempF: "))

    #replace below line with function call to converter()
    #tempC = (tempF - 32) * (5 / 9)

    tempC = converter(tempF)

    #update sumtotal of all tempF values    
    sumtotalTemps += tempF 
    #same as: sumtotalTemps = sumtotalTemps + tempF

    totalTemps += 1
    #totalTemps = totalTemps + 1

    
    print("\tTOTAL TEMPS: ", totalTemps)
    print("\tTemp F is {0:.1f} = Temp C is {1:.1f}".format(tempF, tempC))

    #FOR TESTING --> print("current sum total: ", sumtotalTemps)

    #remove below and replace with function again()

    ans = again()

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

avgTempC = converter(avgTempF)

print("\nTOTAL TEMPERATURES: ", totalTemps)
print("AVERAGE TEMPERATURE: {0:.1f}F | {1:.2f}C".format(avgTempF, avgTempC))

print("\n\nThank you. Goodbye")