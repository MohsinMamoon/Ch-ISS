def coord(pos):

    cols_mapping = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    col = int(cols_mapping[pos[0]])
    row = 8 - int(pos[1])

    return row, col