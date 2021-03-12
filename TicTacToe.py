#!C:\Users\LENOVOTHINKPADW540\AppData\Local\Programs\Python\Python38-32\python.exe

#Import
from random import choice
import os
os.system("cls")
#Create a dict represent the board
board = {}
for i in range(9):
    board[str(i + 1)] = ' '

#Initial variables
test = ''
player1 = ''
already_list =[]

#Print out the board
def print_board(board):
    print('|---------------|')
    print('| ' + board['1'] + ' ' + ' | ' + ' ' + board['2'] + ' ' + ' | ' + ' ' + board['3'] +' |')
    print('|---------------|')
    print('| ' + board['4'] + ' ' + ' | ' + ' ' + board['5'] + ' ' + ' | ' + ' ' + board['6'] +' |')
    print('|---------------|')
    print('| ' + board['7'] + ' ' + ' | ' + ' ' + board['8'] + ' ' + ' | ' + ' ' + board['9'] +' |')
    print('|---------------|')

#Choose who to play first
def who():
    global player1, player2, a, b
    x_and_o = ['X', 'O']
    if choice(x_and_o) == player1:
        a = 'Player 1'
        b = 'Player 2'
        print('Player 1 go first!')
        return a,b
    else:
        a = 'Player 2'
        b = 'Player 1'
        print('Player 2 go first!')
        return a,b


#Check who win
def player_who_win(board):
    global test
    if board[str(i)] == player1:
        print('Player 1 wins the game!')
    else:
        print('Player 2 wins the game!')

def who_win(board, mark):
    global test
    #Check horizontally
    for i in [1,4,7]:
        if board[str(i)] == board[str(i + 1)] == board[str(i + 2)] == mark:
            player_who_win(board)
            again = input('Do you want to play again?\n').upper()
            if again == 'Y':
                test = 'Not End'
            elif again == 'N':
                test = 'End'
    #Check vertically
    for i in [1,2,3]:
        if board[str(i)] == board[str(i + 3)] == board[str(i + 6)] == mark:
            player_who_win(board)
            again = input('Do you want to play again?\n').upper()
            if again == 'Y':
                test = 'Not End'
            elif again == 'N':
                test = 'End'
    #Check diagonally
    if board['1'] == board['5'] == board['9'] == mark:
        player_who_win(board)
        again = input('Do you want to play again?\n').upper()
        if again == 'Y':
            test = 'Not End'
        elif agin == 'N':
            test = 'End'
    elif board['3'] == board['5'] == board['7'] == mark:
        player_who_win(board)
        again = input('Do you want to play again?\n').upper()
        if again == 'Y':
            test = 'Not End'
        elif agin == 'N':
            test = 'End'

#Check number input
def position():
    global x, already_list
    x = ''
    while x not in ['1','2','3','4','5','6','7','8','9']:
        x = input()
        if x not in ['1','2','3','4','5','6','7','8','9'] or x in already_list:
            print('Please choose again!')
            x = ''
            continue
        already_list.append(x)

#Check already list
def check_already_list(already_list):
    already_list = sorted(already_list)
    if already_list == [1,2,3,4,5,6,7,8,9]:
        print('No ones win!')
    
#Let player choose 'X' or 'O'
def x_or_o():
    global player1, player2
    while player1 != 'X' and player1 != 'O':
        player1 = input().upper()
        if player1 != 'X' and player1 != 'O':
            print('Please choose correct mark!')
        if player1 == 'X':
            print('So Player 1 will be X and Player 2 will be O')
            player2 = 'O'
        elif player1 == 'O':
            print('So Player 1 will be O and Player 2 will be X')
            player2 = 'X'

#Main Game

#The Game
while True:
    #Introduction
    if test == 'End':
        break
    print('Welcome to the tic tac toe game!')
    print('Player 1, You choose X or O:')
    player1 = ''
    player2 = ''
    test = ''
    board = {}
    for i in range(9):
        board[str(i + 1)] = ' '
    already_list =[]
    x_or_o()
    #Call out who play first
    who()
    print('Let\'s play!')
    while True:
        print(a + '\'s turn!')
        
        print('What position ' + a + ' want to place at?')
        position()
        if a == 'Player 1':
            board[x] = player1
        else:
            board[x] = player2
        print('\n')
        print_board(board)
        print('\n')
        who_win(board, 'X')
        if test == 'End':
            break
        elif test == 'Not End':
            os.system("cls")
            break
        who_win(board, 'O')
        if test == 'End':
            break
        elif test == 'Not End':
            os.system("cls")
            break
        already_list = sorted(already_list)
        if already_list == ['1','2','3','4','5','6','7','8','9']:
            print('No ones win!')
            again_2 = input('Do you want to play again?\n').upper()
            if again_2 == 'Y':
                test = 'Not End'
                os.system("cls")
                break
            elif again_2 == 'N':
                test = 'End'
                break
        
        print('What position ' + b + ' want to place at?')
        position()
        if b == 'Player 1':
            board[x] = player1
        else:
            board[x] = player2
        print('\n')
        print_board(board)
        print('\n')
        who_win(board, 'X')
        if test == 'End':
            break
        elif test == 'Not End':
            os.system("cls")
            break
        who_win(board, 'O')
        if test == 'End':
            break
        elif test == 'Not End':
            os.system("cls")
            break
        already_list = sorted(already_list)
        if already_list == ['1','2','3','4','5','6','7','8','9']:
            print('No ones win!')
            again_2 = input('Do you want to play again?\n').upper()
            if again_2 == 'Y':
                test = 'Not End'
                os.system("cls")
                break
            elif again_2 == 'N':
                test = 'End'
                break