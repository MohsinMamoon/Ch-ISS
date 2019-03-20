from pieces import Piece
from xy import *
import os

class Board:

    def __init__(self):
        self.board = []
        for i in range(8):
            temp = []
            for j in range(8):
                temp.append(Piece('a1', 'b'))
            self.board.append(list(temp))
    
    def disp(self):
        r = 8
        os.system('cls' if os.name == 'nt' else 'clear')  
        print('\t\t\t', end='')
        for i in ['a','b','c','d','e','f','g','h']:
            print('  ', i, end='')
        print('')      
        strf = ''
        for row in self.board:
            for i in range(2):
                if i%2==0:
                    strf += '\t\t\t '
                else:
                    strf += '\t\t\t'+str(r)
                    r = r-1
                for obj in row:
                    if i%2 == 0: # Print Board Scaffolding
                        strf += '+---'
                    else: # Print objects
                        strf += '|'
                        strf += obj.disp()
                        # strf += ' 0 '
                if i%2 == 0:
                    strf += '+'
                else:
                    strf += '|'
                strf += '\n'
        strf += ' \t\t\t '           
        for obj in self.board[-1]:
            strf += '+---'
        strf += '+'
        print(strf)
        print('\t\t\t', end='')
        for i in ['a','b','c','d','e','f','g','h']:
            print('  ', i, end='')
        print('')
        
    def place(self, piece):
        row, col = coord(piece.pos)
        self.board[row][col] = piece