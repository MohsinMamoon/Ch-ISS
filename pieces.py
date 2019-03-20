class Piece:
    def __init__(self, pos, clr):
        self.pos = pos
        self.color = clr
        self.p_type = 'none'
    #add in more
    def disp(self):
        return "   " 