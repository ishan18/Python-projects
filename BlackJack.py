# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:11:46 2019

@author: RAJNIKANT
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,\
         'Queen':10, 'King':10, 'Ace':11}

class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append((Card(suit,rank)))
    
    def __str__(self):
        return f"{self.deck}"

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand(Card):
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(f"{card}")
        if card.rank=="Ace":
            self.value+=self.aces
        else:
            self.value+=values[card.rank]
        
        
    
    def adjust_for_ace(self):
        if self.value<11:
            self.aces=11
        else:
            self.aces=1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet
        
    def __str__(self):
        return f"You have {self.total} chips left"
    
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("Enter your bet here "))
        except:
            print("OOPS! incorrect input please try again")
        else:
            if chips.bet<=chips.total:
                chips.total-=chips.bet
                break
            else:
                print("Insufficient balance, please enter a lower amount")

def hit(deck,hand):
    #hand.adjust_for_ace()
    hand.add_card(deck.deal())
    
    #return hand.cards[-1].rank=="Ace"
    
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    _=input("'hit' OR 'stand'")
    if _=="hit":
        hit(deck,hand)
        return True
    elif _=="stand":
        playing=False
    else:
        print("you entered a wrong input!, please enter again")
        hit_or_stand(deck,hand)
        
def show_some(player,dealer):
    print("Player's hand are:-")
    for x in player.cards:
        print(f"{x}")
    print("\nDealer's hand:-")
    for x in dealer.cards[1:]:
        print(f"{x}")
    
def show_all(player,dealer):
    print("Player's hand are:-")
    for x in player.cards:
        print(f"{x}")
    print("\nDealer's hand:-")
    for x in dealer.cards:
        print(f"{x}")
        
def player_busts(player):
    if player.value > 21:
        print("Player busts")
        print("Dealer wins!")
        return True
    else:
        return False
    
def player_wins(player,dealer,player_chips):
    if player.value==21:
        print("BlackJack! congratulations")
        player_chips.total+=2*player_chips.bet
        return True
    if dealer_busts(dealer) and not(player_busts(player)) or (21-player.value)<(21-dealer.value):
        print("Player wins")
        player_chips.total+=2*player_chips.bet
        
        return True
    

def dealer_busts(dealer):
    if dealer.value>21:
        print("Dealer busts")
        return True
    
def dealer_wins(player,dealer,player_chips):
    if player_busts(player) or (21-player.value)>(21-dealer.value) and not(push(player,dealer,player_chips)):
        print("dealer wins!")
    
def push(player,dealer,player_chips):
    if dealer.value==player.value:
        player_chips.total+=player_chips.bet
        print("PUSH")
        
        return True

from IPython.display import clear_output
player_chips=Chips()

while True:
    playing=True
    # Print an opening statement
    clear_output()
    print("Welcome to the great game of blackjack\n\n")
    print(player_chips)
    # Create & shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffle()
    player=Hand()
    dealer=Hand()
    player.adjust_for_ace()
    dealer.adjust_for_ace()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
    
        
    # Set up the Player's chips
    
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)

    show_some(player,dealer)
    while playing:
        # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        if hit_or_stand(deck,player):
            hit(deck,dealer)
            
        # Show cards (but keep one dealer card hidden)
        clear_output()
        show_some(player,dealer)
        push(player,dealer,player_chips)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if (player_busts(player)):
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while dealer.value<17:
        dealer.add_card(deck.deal())
    
        # Show all cards
    clear_output()
    show_all(player,dealer)
    # Run different winning scenarios
    if not(player_wins(player,dealer,player_chips)):
            
        dealer_wins(player,dealer,player_chips)
        
        
    
    # Inform Player of their chips total 
    print(player_chips)
    # Ask to play again
    p=input("Do you want to play again 'yes' or 'no'? ")
    if p=="no":
        break