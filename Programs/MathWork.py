#=======================================================================================================================================
#Description:
#This code is to be used for math homework. More equations formulas will be added in the form of functions 
#User will choose from a menu the desired equation calculator, input values, and the program will show work and correct answer 
#=======================================================================================================================================

#Function for program to show work for equations
#=======================================================================================================================================
def showWork (topics, steps): 
    print("Showing Work")#Prints to user that function is showing work
    print("=" * 20)#Formatting
    print(f"Topics: -> {topics}") #Prints topic. Topic = what math subject is being calculated (Slope, Pythagorean therom etc)
    for step in steps:#For loop that handles the steps in the equation for any given function. Will show all steps program took to solve equation and then display them to user. 
        print("" + step) #Used to correctly lable out which steps (Step 1, Step 2 etc)
    print("=" * 20)
#=======================================================================================================================================
def slopeCalc(): #Function used to calculate slope
    print("Slope = (y2 - y1) / (x2-x1)") #Prints out the slope formula 
    y2 = float(input("y2:"))#User inputs the value of the y2
    y1 = float(input("y1: "))#User inputs the value of the y1
    x2 = float(input("x2:"))#User inputs the value of the x2
    x1 = float(input("x1:"))#User inputs the value of the x1

    steps = [ f" Slope Formula = (y2-y1) / (x2-x1)",#This is how program will show steps in showing work 
       f" Plug in : ({y2} - {y1}) / ({x2} - {x1})"]#This is how the program will know where to put the values the user input into the program. The program will properly plug values into y2-y1 and dsiplay whatever the user input. 
    
    if x2 - x1 == 0:#If statement to handle if the total of x2-x1 is equal to zero 
        steps.append("Slope is Undefined")#Appends the answers to steps list 
        showWork("Slope", steps) 
        print("Slope is Undefined")#Prints to user that the answer is Undefined because it equals zero 

    else: 
        slope = (y2 - y1) / (x2 - x1) 
        steps.append(f"Slope: = {slope}")
        showWork( "Slope", steps)
        print(f"Slope: {slope}")
#=======================================================================================================================================
#Function to allow user to contiune using program
#=======================================================================================================================================
def userContiune():
    answer = input("Do you want to solve another problem? (y\n): ").lower() 
    if answer == "y":
        showMenu()
    else:
        print("Loser") 
        
#Function that displays menu, allowing the user to decide what they want the program to do
#=======================================================================================================================================
def showMenu():#Function for showing the menu to the user 
    print("Math helper")
    print("=" *20)
    print("1. Slope")
    print("2. Place holder")
    print("3. Exit")

    choice = input("Choose option 1-3:")#Variable (choice) that is used 

    if choice == "1":
        slopeCalc()

    elif choice == "2":
        print("Option not available yet")

    elif choice == "3": 
        print("Thank you")
        return   

showMenu()#Redirects the program back to show the menu to the user 