#Tyler Mattson 
#Course Project  
#Section: SE126 - 202502 (Morning Class) 
#Date: Febuary 18th 2025

import random 

suits = [ 'Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3' , '4' , '5' , '6' ,'7', '8', '9', '10', 'Jack' , 'King' , 'Queen', 'Ace'  ]
values = ['2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11 ] 

def createDeck(): 
    deck = [] 
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck 

def calchandValue(hand): 
    value = 0 
    ace = 0 
    for card in hand: 
        value += values[card[0]]
        if card[0] == 'Ace': 
            ace += 1 
    while value > 21 and ace: 
        value -= 10 
        ace -= 1 
    return value 

def dealfirstCard(deck): 
    playerHand = [deck.pop(), deck.pop()] 
    dealerHand = [deck.pop(), deck.pop()]
    return playerHand, dealerHand 

def listCard(hand,deck):
    hand.append(deck.pop())

       
    



