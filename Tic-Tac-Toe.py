# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:17:12 2019

@author: RAJNIKANT
"""

import random

def display_board(board):
    print("\n"*100)
    print(" {} | {} | {} ".format(board[7],board[8],board[9]))
    print("-"*11)
    print(" {} | {} | {} ".format(board[4],board[5],board[6]))
    print("-"*11)
    print(" {} | {} | {} ".format(board[1],board[2],board[3]))

def player_input():
    player1=input("Enter player 1's symbol (X or O): ")
    if not(player1 in ("X","O")):
        print("Please Enter a valid symbol")
        player_input()
    return player1

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    out=[]
    for i in range(1,8,3):
        out.append(board[i]==board[i+1]==board[i+2]==mark)
    for i in range(1,4):
        out.append(board[i]==board[i+3]==board[i+6]==mark)
    out.append(board[1]==board[5]==board[9]==mark)
    out.append(board[3]==board[5]==board[7]==mark)
    return True in out

def choose_first():
    x=random.randint(1,2)
    print("Player {} will go first".format(x))
    return x

def space_check(board, position):
    return board[position]==" "

def full_board_check(board):
    return " " in set(board)

def player_choice(board):
    position=int(input("Enter a position on the tic tac toe board"))
    if position not in range(1,10):
        print("Enter a valid position")
        player_choice(board)
    if space_check(board,position):
        return position
    else:
        print("Sorry! that position is pre-occupied please enter another one")
        return True

def replay():
    ask=input("Do you want to play again, 'yes' or 'no'?: ")
    #if ask not in ("yes","no"):
     #   print("please enter a valid answer")
      #  return 0
    return ask=='yes'

def turn(player,pla_num):
    print("Player {}'s turn".format(pla_num))
    _=player_choice(board)
    if _==True:
        player_choice(board)
    place_marker(board,player,_)
    display_board(board)
    if win_check(board,player):
        print("Congratulations! player {} wins".format(pla_num))
        return True

#game 
    
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board=["#"," "," "," "," "," "," "," "," "," "]
    player1=player_input()
    if player1=="X":
        player2="O"
    elif player1=="O":
        player2="X"
    x=choose_first()
    #pass
    display_board(board)
    while (full_board_check(board)):
        
        if x==1:
            #Player 1 Turn
            if turn(player1,1):
                break
            # Player2's turn.
            if turn(player2,2):
                break
        else:
            #player 2 Turn
            if turn(player2,2):
                break
            #Player 1 Turn
            if turn(player1,1):
                break
    else:
        print("DRAW!")
    
    if not(replay()):
        break