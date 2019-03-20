from xy import *
from pieces import Piece

class Bishop(Piece):
    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.p_type = 'bishop'
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
            return ' B.'
        else:
            return '.B '

    def valid(self, initial, final, capture):
        ri,ci = coord(initial)
        rf,cf = coord(final)
        if abs(ri-rf) == abs(cf-ci) and rf-ri != 0:
            return True
        else:
            return False