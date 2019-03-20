from xy import *
from pieces import Piece

class Queen(Piece):
    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.p_type = 'queen'
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
            return ' Q.'
        else:
            return '.Q '

    def valid(self, initial, final, capture):
        ri, ci = coord(initial)
        rf, cf = coord(final)
        if abs(rf-ri) == abs(cf-ci) and rf-ri != 0:
            return True
        elif (abs(rf-ri) != 0 and cf-ci == 0) or (rf-ri == 0 and abs(cf-ci) != 0):
            return True
        else:
            return False