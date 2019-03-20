from board import Board
from pieces import *
from xy import coord
from pawn import Pawn
from rook import Rook
from knight import Knight
from king import King
from bishop import Bishop
from queen import Queen
import os

mov = True

def p_move(brd, initial, final, turn):
    if turn:
        color = 'Black'
    else:
        color = 'White'
    
    ri, ci = coord(initial)
    rf, cf = coord(final)
    
    oi = brd.board[ri][ci]
    of = brd.board[rf][cf]
    if(oi.color != color or of.color == color):
        return turn
    
    if of.p_type == 'none':
        capture = False
    else:
        capture = True
    if oi.move(initial, final, capture):
        brd.place(oi)
        brd.place(Piece(initial, 'none'))
        turn = not turn    
        if of.p_type == 'king':
            turn = 'end'
    return turn


B = Board()
for i in ['a','b','c','d','e','f','g','h']:
    B.place(Pawn(i+'2', 'Black'))
    B.place(Pawn(i+'7', 'White'))
for i in ['a', 'h']:
    B.place(Rook(i+'1', 'Black'))
    B.place(Rook(i+'8', 'White'))
for i in ['b', 'g']:
    B.place(Knight(i+'1','Black'))
    B.place(Knight(i+'8', 'White'))
for i in ['c', 'f']:
    B.place(Bishop(i+'1', 'Black'))
    B.place(Bishop(i+'8', 'White'))
for i in ['d']:
    B.place(King(i+'1', 'Black'))
    B.place(King(i+'8', 'White'))
for i in ['e']:
    B.place(Queen(i+'1', 'Black'))
    B.place(Queen(i+'8', 'White'))

turn = True
print("\nWelcome To Ch-ISS\n\n \t\t This is a game made in python!\n\n\n")
P1 = input('Enter Name of Player 1(bottom): ')
P2 = input('Enter Name of Player 2(top): ')
board = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

os.system('cls' if os.name == 'nt' else 'clear')
B.disp()

while True:
    mov = True
    curr_turn = turn
    if turn:
        print('%s\'s turn(P.)--->' % P1)
    else:
        print('%s\'s turn(P.)--->' % P2)
    
    act = input()
    if act[0] == 'q':
        break
    if len(act) != 5 or (act[0] not in board) or (act[3] not in board) or (int(act[1]) not in range(1,9)) or (int(act[4]) not in range(1,9)) or (act[2] not in [' ']):
        print("Invalid Move!")
        continue

    turn = p_move(B, act[0:2], act[3:5], turn)
    if curr_turn == turn:
        print("Invalid Move!")
    elif turn == 'end':
        if curr_turn:
            winner = P1
        else:
            winner = P2
        print("\n\t\t\t",winner," WINS!\n")
        break
    else:
        B.disp()
