from get_pos_rest import get_pos

while True:
    if get_pos() == None:
        print("\rAnalizing to trade...", end = '')
    else:
        print("There is already a position open: ", get_pos())