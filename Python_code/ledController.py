from Python_code.ledDBConnection import dbConnect


def ledControl(color, mode):

    r = 0
    g = 0
    y = 0
    dbConnect(r, g, y)
