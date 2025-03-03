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
    deck = [] #creates empty dictionary
    with open(filename) as csvfile: #Opening CSV file 
        file = csv.reader(csvfile)

        for rec in file: 
            value = rec[0]
            suit = rec[1]
            color = rec[2]
            deck.append((value, suit, color))
    random.shuffle(deck)
    return deck 
       

def deckCreate(): 
    color = ["Red", "Black"]
    suits = ["Hearts", "Diamonds", "Club", "Spade"]
    scoreValue = []
    for n in range(2,11): 
        scoreValue.append((str(n) , n))
    cardFace = ["Jack", "Queen", "King"]
    for face in cardFace: 
        scoreValue((face,10))
    scoreValue.append(("Ace", 11))
    deck = []
    for suit in suits: 
        color = "Red" if suit in ["Hearts", "Diamonds"] else "Black" 
        for value, numValue in value:  
            deck.append((scoreValue, suit, color, numValue))
    deck *= 4
    random.shuffle(deck)
    return deck 

def calcScore(hand):
    total =  sum(card[2] for card in hand)
    if total > 21 and any(card[1] == 11 for card in hand): 
        total -= 10 
    return total 

def playBlackjack(deck, playerHand, dealerHand, balance, earnings): 
    print(f"Your hand: {playerHand} | Score: {calcScore(playerHand)}")
    if dealerHand:
        print(f"Dealer's hand: {dealerHand[0]}, ('Hidden')")
    else: 
        print("Dealer's hand: ('Hidden')")

    if calcScore(playerHand) == 21: 
        print("BlackJack, you win!")
        balance += 50 
        earnings.append(balance)
        return nextRound(deck, balance, earnings)
    
    action = input ("Hit or Stand? (h/s): ").strip().lower()

    if action == "h": 
        playerHand.append(deck.pop())
        if calcScore(playerHand) > 21: 
            print(f"Bust! Final score : {calcScore(playerHand)}")
            balance -= 10
        return playBlackjack(deck, playerHand, dealerHand, balance, earnings)

    while calcScore (dealerHand) < 17: 
        dealerHand.append(deck.pop())
    print(f"Dealer's hand: {dealerHand} | Score: {calcScore(dealerHand)}")

    dealerBust = calcScore(dealerHand) > 21 
    playerWin = calcScore(playerHand) > calcScore(dealerHand) 

    if dealerBust or playerWin: 
        print("You win!")
        balance += 20 
    else: 
        print("You lose")
        balance += 10 

    earnings.append(balance)
    return nextRound(deck, balance, earnings)

def nextRound(deck, balance, earnings): 
    if len(deck) <10: 
        deck = ()

    playAgain = input("Play again? (y/n): ").strip().lower()
    if playAgain == "y": 
        return playBlackjack(deck, [deck.pop() , deck.pop(), deck.pop()], balance, earnings) #deck.pop() is used for each card, two for the player one for the visible dealer card 
    
    else: 
        saveEarnings(earnings)
        print("Game Over. Your final balance is:", balance)

def saveEarnings(earnings): 
    with open ("earnings.csv", "w") as file: 
        writer = csv.writer(file)
        writer.writerow(["Earnings"])
        for amount in earnings: 
            writer.writerow([amount])

filename = "text files/cards.csv"
deck = loadDeck(filename)

playBlackjack(deck, [deck.pop(), deck.pop(), deck.pop()], dealerHand = [], balance = 100, earnings = [])