from xy import *
from pieces import Piece

class Rook(Piece):
    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.p_type = 'rook'
    def move(self, initial, final, capture):
        try:
            assert(self.pos == initial)
        except:
            return False
        if self.valid(initial, final, capture):
            self.pos = final
            return True

    def disp(self):
        if self.color == 'Black':
            return ' R.'
        else:
            return '.R '

    def valid(self, initial, final, capture):
        ri,ci = coord(initial)
        rf,cf = coord(final)
        if (ri-rf==0 and ci-cf!=0) or (ri-rf!=0 and ci-cf==0):
            return True
        else:
            return False