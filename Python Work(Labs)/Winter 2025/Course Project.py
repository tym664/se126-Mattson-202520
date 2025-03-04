#Tyler Mattson 
#Course Project  
#Section: SE126 - 202502 (Morning Class) 
#Date: March 1rst 2025

#VARIABLE DICTIONARY
#======================================================================================================

#======================================================================================================

#DESCRIPTION
#=========================================================================================================================================================
#This program is a game of BlackJack 
#The program utilizes two imports. Import CSV to import the CSV file that contains the card number, the card face, and the color of the card. 
#The program utilizes the random import to randomize the cards given to the player and dealer. The color and card faces are tied together.
#Red cards will only appear as either a Diamond or Hearts, but the order in which they appear will be random
#Black cards will only appear as either a Spade or Club, but the order in which they appear will be random
#The user has the option to pick the Ace as either 1 or 11. The user will be given a choice when the Ace card is selected by the program. 
#What-ever the user chooses (1 or 11) the decision the player made will follow the player throught their turn until the player or dealer bust (aceDec)
#This program uses various function, the functions have various parameters that hold data through other functions
#The parameters can change depending on the user input (Which Ace number the user picks, how much the player wins or looses)
#After the program is finshed, the program will create a CSV file with the players winngs from playing through BlackJack 
#Be careful. You can go into debt!
#=========================================================================================================================================================

import random #Imports random function to randomize cards given to player or dealer 
import csv #Imports CSV file with card data 

def loadDeck(filename): #filename represents the path of the file being imported 
    deck = [] #creates empty list for storing the deck 
    with open(filename) as csvfile: #Opening CSV file 
        file = csv.reader(csvfile)
        for rec in file: 
            value, suit, color = rec #Pulls data from each row in CSV file 
            deck.append((value, suit, color)) #Appends the cards to the deck 
    random.shuffle(deck) #Shuffles the deck to randomize the order of the cards 
    return deck #Returns shuffled deck 
       

def deckCreate(card, role, aceDec): #Function to determine the numeric value of the card based on the face of the card 
    #card faces  --> (Jack, Queen, King and Ace)
    value = card[0] #Imports the value of the card from the CSV file 
    if value in ["Jack", "Queen", "King"]: 
        return 10 #Jack, Queen and King cards are worth 10 points 
    elif value == "Ace" and role == "player": 
        if card not in aceDec: #Checks if the ace decision was made 
            aceValue = input("Would you like your ace to be a 1 or an 11?") #Asks user what they want the ace value to be 
            aceDec[card] = 1 if aceValue == "1" else 11 #Stores users Ace decision 
        return aceDec[card]
    elif value == "Ace":
        return 11 #Dealer's ace will always be 11. The function automatically assigns 11 points to dealer's hand 
    else: 
        return int(value) #Converts card values into integers 


def calcScore(hand, role, aceDec): #Function to determine the total score of the hand
    total =  sum(deckCreate(card,role, aceDec) for card in hand) #Adds card vaules together 
    aceCount = sum(1 for card in hand if card[0] == "Ace" and role == "player") #Adjusting player score if player has Ace 
    while total > 21 and aceCount > 0: 
        total -= 10 #Adjusts Ace value from 11 ot 1 if total hand value exceeds 21 
        aceCount -= 1 #Reduces Ace count 
    return total #Returns the final score 


def playBlackjack(deck, playerHand, dealerHand, balance, earnings, filename, aceDec): #Function to run the game of BlackJack 
    #Variables are passed through to keep track and reload the deck if needed. 
    print(f"Player hand: {playerHand}") #Displays players hand 
    print(f"Player Card Total: {calcScore(playerHand, 'player', aceDec)}")# Displays player's score 
    print("=" * 35)#Formating 
    print(f"Dealer's hand : {dealerHand}") #Displays dealer's hand 
    print(f"Dealer's Card Total : {calcScore(dealerHand, 'dealer', aceDec)}")#Displays dealer's score 
    print("=" * 35)#Formating 
    if calcScore(playerHand, 'player', aceDec) == 21: 
        print("BlackJack, you win!") #Player wins 
        balance += 550 #Player earns 550 credits 
        earnings.append(balance) #Updates earnings history 
        return nextRound(deck, balance, earnings, filename) #Program moves onto the next round 
    action = input ("Hit or Stand? (h/s): ").strip().lower() #Asks the player what they want their action to be 
    while action == "h": #Player chooses to hit 
        if not deck: #Checks if the deck is empty before populating 
            deck = loadDeck(filename) #If deck is empty, program will re-load loadDeck function to pull data from CSV 
        playerHand.append(deck.pop()) #Adds a new card to players hand 
        print(f"Player's hand: {playerHand}") #Prints players new hand 
        print(f"Player's Score: {calcScore(playerHand, 'player', aceDec)}") #Shows player's new score
        print("=" * 35) #Formatting 
        if calcScore(playerHand, 'player', aceDec) > 21: 
            print("BUST")#Player looses if score is higher than 21 
            balance -= 350 #Player looses 350 credits 
            return nextRound(deck, balance, earnings, filename) #Program moves onto the next round 
        action = input("Hit or Stand? (h/s): ").strip().lower() #Program asks player for next input (hit or stand)
    while calcScore (dealerHand, 'dealer', aceDec) < 17: #Dealer draws cards untill score is less than 17 
        if not deck: #Checks if deck is empty before populating 
            deck = loadDeck(filename) #If deck is empty, program will populate by calling the loadDeck function, program will pull data from CSV file again 
        dealerHand.append(deck.pop()) #Adds new cards to dealers hand
    print(f"Final Dealer's hand: {dealerHand}")#Shows dealer's final hand 
    print(f"Final Dealer's Score: {calcScore(dealerHand, 'dealer', aceDec)}") #Shows dealer's final score 
    print("=" * 35)
    dealerBust = calcScore(dealerHand, 'dealer', aceDec) > 21 
    playerWin = calcScore(playerHand, 'player', aceDec) > calcScore (dealerHand, 'dealer', aceDec)
    if dealerBust or playerWin: #Conditional statements for if the player wins or looses
        print("YOU WIN")#Player won
        balance += 200 #Player wins 200 credits 
    else: 
        print("You lose")#Player lost 
        balance -= 400 #Player looses 400 credits  
    earnings.append(balance) #Updates earnings history 
    return nextRound(deck, balance, earnings, filename) #Program moves onto the next round 


def nextRound(deck, balance, earnings, filename): #Function to handle if the player wants to play again or exit program 
    if len(deck) <10: #Reloads the deck if few too many cards remain 
        print("Reloading deck....")#Notifying user that the cards are re-shuffeling 
        deck = loadDeck(filename) #Re-calling function that loads the CSV file to restart data flow
    playAgain = input("Play again? (y/n): ").strip().lower()#User input
    print()#Formatting 
    if playAgain == "y": #Staring next round 
        if len(deck) < 4: #Checks to make sure there are atleast 4 cards before staring round 
            deck = loadDeck(filename) #if there are not 4 cards, program will reload CSV file (filename) with the loadDeck function 

            #Player and dealer are dealt two hands (deck.pop())
            #filename variable is being passed through the program to be reloaded if needed (reshuffling deck, population error correction)
            #aceDec variable is used to keep track of players decision (if the player chose either a 1 or an 11)
            #balance and earnings variables are used to keep track of players earnings and total balance throughout the game 
        return playBlackjack(deck, [deck.pop(), deck.pop()], [deck.pop(), deck.pop()], balance, earnings, filename, aceDec)#Function to play BlackJack 
    else: 
        saveEarnings(earnings) #Saves the players earnings through-out the game 
        print("Game Over") 
        print("Your final balance is:", balance) #Calls balance list to update the player's balance
        #Displays the final balance of the player's credits


def saveEarnings(earnings): #Function to write/save players earings into a new CSV file 
    with open ("BlackJack_Credits.csv", "w") as file: #Opens a new file in write ("w") mode 
        writer = csv.writer(file)
        writer.writerow(["BlackJack Earnings"]) #Writes the header in the new file 
        for amount in earnings: 
            writer.writerow([amount]) #Saves the players balance entry 


filename = "text files/cards.csv" #Function call to open the CSV file for the program. Path to the CSV file 
deck = loadDeck(filename) #Function call to load and shuffle the deck. Data is pulled from the CSV file 

if len(deck) < 4: #Ensures there are enough cards availiable before starting the game 
    deck = loadDeck(filename) #If there are not enough cards, program will call loadDeck function to re-load CSV file(filename) 
aceDec = {} #Stores the player's Ace decision 

#Starts the game. Player recieves a balance of 600 credits and the players earnings history is not saved. 
playBlackjack(deck, [deck.pop(), deck.pop()], [deck.pop(), deck.pop()], 600, [], filename, aceDec) 
#600 is the amount of credits the player will recieve 
#[] is an empty list to store the players earnings from each round 
#aceDec is used to track player ace decision 
#filename variable holds the CSV path, will reload the deck if cards get low 