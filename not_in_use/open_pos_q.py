

def open_pos_input():

    print("----Open position----")

while True:
    codigo=''
    eleccion = input("Quieres abrir una posicion? Presiona Y o N ")
    while True:
        open_p = eleccion.lower()
        if open_p == 'y':
            open_p = "y"
            break
        elif open_p =='n':
            open_p = 'n'
            break
        else:
            eleccion = input("Quieres abrir una posicion? Presiona Y o N ")
    
    if open_p == 'y':
        eleccion = input("Presiona L para Long o S para Short")
        while True:
            direction_p = eleccion.lower()
            if direction_p == 'l':
                direction_p = "Buy"
                break
            elif direction_p == "s":
                direction_p = 'Sell'
                break
            else: eleccion = input("Presiona L para Long o S para Short")
    else:
        break
    
    if direction_p == 'Buy' or 'Sell':
        eleccion = input("Quieres establecer un Stop Loss?")
        while True:
            sl = eleccion.lower()
            if sl == 'y':
                sl = 'y'
                break
            elif sl == 'n':
                sl = 'n'
                break
            else: eleccion = input("Quieres establecer un Stop Loss?")
    else:
        break
    
    if sl == 'y':
        stop_l = input("Ingrese porcentaje de Stop Loss")

    if direction_p == 'l' or 's':
        eleccion = input("Quieres establecer un Take Profit?")
        while True:
            tp = eleccion.lower()
            if tp == 'y':
                tp = 'y'
                break
            elif tp == 'n':
                tp = 'n'
                break
            else: eleccion = input("Quieres establecer un Take Profit?")
    else:
        break

    if tp == 'y':
        take_p = input("Ingrese porcentaje de Take Profit")
    break

        
