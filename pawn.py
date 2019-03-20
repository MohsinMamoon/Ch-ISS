from xy import *
from pieces import Piece

class Pawn(Piece):
    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.p_type = 'pawn'
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
            return ' P.'
        else:
            return '.P '

    def valid(self, initial, final, capture):
        ri,ci = coord(initial)
        rf,cf = coord(final)

        if self.color == 'Black':
            if capture:
                if ri-rf == 1 and abs(cf-ci) == 1:
                    return True
                else:
                    return False
            else:
                if cf-ci == 0:
                    if ri == 6:
                        if ri-rf == 1 or ri-rf == 2:
                            return True
                        else:
                            return False
                    else:
                        if ri-rf == 1:
                            return True
                        else:
                            return False
                else:
                    return False
        else:
            if capture:
                if rf-ri == 1 and abs(cf-ci) == 1:
                    return True
                else:
                    return False
            else:
                if cf-ci == 0:
                    if ri == 1:
                        if rf-ri == 1 or rf-ri == 2:
                            return True
                        else:
                            return False
                    else:
                        if rf-ri == 1:
                            return True
                        else: 
                            return False
                else:
                    return False