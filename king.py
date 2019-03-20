from xy import *
from pieces import Piece

class King(Piece):
    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.p_type = 'king'
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
            return ' K.'
        else:
            return '.K '

    def valid(self, initial, final, capture):
        ri, ci = coord(initial)
        rf, cf = coord(final)
        if rf-ri == 0 and cf-ci == 0:
            return False
        elif abs(rf-ri) <= 1 and abs(cf-ci) <= 1:
            return True
        else:
            return False