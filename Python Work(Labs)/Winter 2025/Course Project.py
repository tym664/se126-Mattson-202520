#Tyler Mattson 
#Course Project  
#Section: SE126 - 202502 (Morning Class) 
#Date: March 1rst 2025

#VARIABLE DICTIONARY
#======================================================================================================

#======================================================================================================

#DESCRIPTION
#=================================================================================================================================================

#=================================================================================================================================================

import random 
import csv


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
    value = card[0] #Imports the value of the card from the CSV file 
    if value in ["Jack", "Queen", "King"]: 
        return 10 #Jack, Queen and King cards are worth 10 points 
    elif value == "Ace" and role == "player": 
        if card not in aceDec: #Checks if the ace decision was made 
            aceValue = input("Would you like your ace to be a 1 or an 11?") #Asks user what they want the ace value to be 
            aceDec[card] = 1 if aceValue == "1" else 11 #Stores users decision 
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
    print(f"Your hand: {playerHand} | Score: {calcScore(playerHand, 'player', aceDec)}")# Displays player's hand and score 
    print(f"Dealers hand : {dealerHand} | Score: {calcScore(dealerHand, 'dealer', aceDec)}")#Displays dealer's hand and score 
    if calcScore(playerHand, 'player', aceDec) == 21: 
        print("BlackJack, you win!") #Player wins 
        balance += 50 #Player earns 50 credits 
        earnings.append(balance) #Updates earnings history 
        return nextRound(deck, balance, earnings, filename) #Program moves onto the next round 
    action = input ("Hit or Stand? (h/s): ").strip().lower() #Asks the player what they want their action to be 
    while action == "h": #Player chooses to hit 
        if not deck: 
            deck = loadDeck(filename) #Checks if the deck is empty before populating 
        playerHand.append(deck.pop()) #Adds a new card to players hand 
        print(f"Your hand: {playerHand} | Score: {calcScore(playerHand, 'player', aceDec)}") #Shows player's new hand 
        if calcScore(playerHand, 'player', aceDec) > 21: 
            print("Bust")#Player looses if score is higher than 21 
            balance -= 10 #Player looses 10 credits 
            return nextRound(deck, balance, earnings, filename) #Program moves onto the next round 
        action = input("Hit or Stand? (h/s): ").strip().lower() #Program asks player for next input

    while calcScore (dealerHand, 'dealer', aceDec) < 17: #Dealer draws cards untill score is equal to 17 
        if not deck: #Checks if deck is empty before populating 
            deck = loadDeck(filename) #Checks if the deck is empty before populating 
        dealerHand.append(deck.pop()) #Adds new cards to dealers hand
    print(f"Final Dealer's hand: {dealerHand} | Final Dealer's Score: {calcScore(dealerHand, 'dealer', aceDec)}") #Shows dealer's final hands and score 
    dealerBust = calcScore(dealerHand, 'dealer', aceDec) > 21 
    playerWin = calcScore(playerHand, 'player', aceDec) > calcScore (dealerHand, 'dealer', aceDec)
    if dealerBust or playerWin: 
        print("You win")
        balance += 20 #Player wins 20 credits 
    else: 
        print("You lose")
        balance -= 10 #Player looses 10 credits  
    earnings.append(balance) #Updates earnings history 
    return nextRound(deck, balance, earnings, filename) #Program moves onto the next round 


def nextRound(deck, balance, earnings, filename): #Function to handle if the player wants to play again or exit program 
    if len(deck) <10: #Reloads the deck if few too many cards remain 
        print("Reloading deck....")
        deck = loadDeck(filename) #Re-calling function that loads the CSV file 

    playAgain = input("Play again? (y/n): ").strip().lower() 
    if playAgain == "y": #Staring next round 
        if len(deck) < 4: 
            deck = loadDeck(filename) #Ensures there are 4 cards before starting the program 

            #Player and dealer are dealt two hands (deck.pop())
            #filename variable is being passed to be reloaded if needed 
            #aceDec variable is used to keep track of players decision 
            #balance and earnings variables are used to keep track of players earnings and total balance throught the game 
        return playBlackjack(deck, [deck.pop(), deck.pop()], [deck.pop(), deck.pop()], balance, earnings, filename, aceDec)#Function to play BlackJack is being called 
    else: 
        saveEarnings(earnings) #Saves the players earnings through-out the game 
        print("Game Over. Your final balance is:", balance) #Displays the final balance of the players credits 


def saveEarnings(earnings): #Function to write/save players earings into a new CSV file 
    with open ("earnings.csv", "w") as file: #Opens a new file in write ("w") mode 
        writer = csv.writer(file)
        writer.writerow(["Earnings"]) #Writes the header in the new file 
        for amount in earnings: 
            writer.writerow([amount]) #Saves the players balance entry 


filename = "text files/cards.csv" #Function call to open the CSV file for the program. Path to the CSV file 
deck = loadDeck(filename) #Function call to load and shuffle the deck. Data is pulled from the CSV file 

if len(deck) < 4: #Ensures there are enough cards availiable before starting the game 
    deck = loadDeck(filename)
aceDec = {} #Stores the player's Ace decision 
#Starts the game. Player recieves a balance of 100 credits and the players earnings history is not saved. 
playBlackjack(deck, [deck.pop(), deck.pop()], [deck.pop(), deck.pop()], 100, [], filename, aceDec) 
#100 is the amount of credits the player will recieve 
#[] is an empty list to store the players earnings from each round 
#aceDec is used to track player ace decision 
#filename variable holds the CSV path, will reload the deck if cards get low 