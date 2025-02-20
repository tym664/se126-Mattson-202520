#Tyler Mattson 
#Course Project  
#Section: SE126 - 202502 (Morning Class) 
#Date: Febuary 18th 2025

import random 


def createDeck():
    suits = [ 'Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3' , '4' , '5' , '6' ,'7', '8', '9', '10', 'Jack' , 'King' , 'Queen', 'Ace' ]
    deck = [(value, suit) for value in values for suit in suits ] 

def cardValue(card): 
    value = card[0]
    if value in ['Jack', 'King', 'Queen']:
        return 10 
    elif value == 'Ace': 
        return 11
    else: 
        return int(value)
    






       
    



