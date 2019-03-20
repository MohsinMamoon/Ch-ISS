from xy import *
from pieces import Piece

class Knight(Piece):
    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.p_type = 'knight'
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
            return ' $.'
        else:
            return '.$ '

    def valid(self, initial, final, capture):
        ri, ci = coord(initial)
        rf, cf = coord(final)

        if(abs(rf-ri)==2 and abs(cf-ci)==1) or (abs(rf-ri)==1 and abs(cf-ci)==2):
            return True
        else:
            return False