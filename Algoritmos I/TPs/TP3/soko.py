PARED = "#"
CAJA = "$"
JUGADOR = "@"
OBJETIVO = "."
OBJETIVO_CON_CAJA = "*"
OBJETIVO_CON_JUGADOR = "+"
CELDA_VACIA = " "


def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador

    Ejemplo:

    >>> crear_grilla([
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ])
    '''
    grilla = []
    for i in desc:
        fila = []
        for j in i:
            fila.append(j)
        grilla.append(fila)
    return grilla           # devuelve una lista de listas

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    return (len(grilla[0]), len(grilla))

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return grilla[f][c] == PARED

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] == OBJETIVO or grilla[f][c] == OBJETIVO_CON_CAJA or grilla[f][c] == OBJETIVO_CON_JUGADOR

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return grilla[f][c] == CAJA or grilla[f][c] == OBJETIVO_CON_CAJA

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    
    return grilla[f][c] == JUGADOR or grilla[f][c] == OBJETIVO_CON_JUGADOR

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for lista in grilla:
        for elem in lista:
            if elem == OBJETIVO_CON_JUGADOR or elem == OBJETIVO:
                return False
    return True

def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.

    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:

    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur

    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.
    '''
    # hacemos una copia de la grilla
    nueva_grilla = crear_grilla(grilla)

    y, x = encontrar_jugador(grilla)
    mx, my = direccion

    # movimiento de celda vacia a ==>
    if nueva_grilla[y][x] == JUGADOR:
        # ==> celda vacia
        
        if nueva_grilla[y+my][x+mx] == CELDA_VACIA:
            nueva_grilla[y + my][x + mx] = JUGADOR
            nueva_grilla[y][x] = CELDA_VACIA
            return nueva_grilla

        # ==> objectivo
        elif nueva_grilla[y + my][x + mx] == OBJETIVO:
            nueva_grilla[y + my][x + mx] = OBJETIVO_CON_JUGADOR
            nueva_grilla[y][x] = CELDA_VACIA
            return nueva_grilla

        # ==> caja sin objetivo
        elif nueva_grilla[y + my][x + mx] == CAJA:
            if nueva_grilla[y + my*2][x + mx*2] == CELDA_VACIA:
                nueva_grilla[y + my*2][x + mx*2] = CAJA
                nueva_grilla[y + my][x + mx] = JUGADOR
                nueva_grilla[y][x] = CELDA_VACIA
                return nueva_grilla

            elif nueva_grilla[y + my*2][x + mx*2] == OBJETIVO:
                nueva_grilla[y + my*2][x + mx*2] = OBJETIVO_CON_CAJA
                nueva_grilla[y + my][x + mx] = JUGADOR
                nueva_grilla[y][x] = CELDA_VACIA
                return nueva_grilla

            else:
                return nueva_grilla
                
        # ==> caja con objetivo
        elif nueva_grilla[y + my][x + mx] == OBJETIVO_CON_CAJA:
            if nueva_grilla[y + my*2][x + mx*2] == CAJA:
                return nueva_grilla
            elif nueva_grilla[y + my*2][x + mx*2] == OBJETIVO_CON_CAJA:
                return nueva_grilla
            elif nueva_grilla[y + my*2][x + mx*2] == PARED:
                return nueva_grilla

            elif nueva_grilla[y + my*2][x + mx*2] == OBJETIVO:
                nueva_grilla[y + my*2][x + mx*2] = OBJETIVO_CON_CAJA
                nueva_grilla[y + my][x + mx] = OBJETIVO_CON_JUGADOR
                nueva_grilla[y][x] = CELDA_VACIA
                return nueva_grilla

            else:
                nueva_grilla[y + my*2][x + mx*2] = CAJA
                nueva_grilla[y + my][x + mx] = OBJETIVO_CON_JUGADOR
                nueva_grilla[y][x] = CELDA_VACIA
                return nueva_grilla
        else:
            return nueva_grilla
           
    # movimiento de objetivo a ==>
    else:
        # ==> celda vacia
        if nueva_grilla[y + my][x + mx] == CELDA_VACIA:
            nueva_grilla[y + my][x + mx] = JUGADOR
            nueva_grilla[y][x] = OBJETIVO
            return nueva_grilla
        # ==> objetivo
        elif nueva_grilla[y + my][x + mx] == OBJETIVO:
            nueva_grilla[y + my][x + mx] = OBJETIVO_CON_JUGADOR
            nueva_grilla[y][x] = OBJETIVO
            return nueva_grilla

        # ==> caja
        elif nueva_grilla[y + my][x + mx] == CAJA:
            if nueva_grilla[y + my*2][x + mx*2] == CELDA_VACIA:
                nueva_grilla[y + my*2][x + mx*2] = CAJA
                nueva_grilla[y + my][x + mx] = JUGADOR
                nueva_grilla[y][x] = OBJETIVO
                return nueva_grilla
            elif nueva_grilla[y + my*2][x + mx*2] == OBJETIVO:
                nueva_grilla[y + my*2][x + mx*2] = OBJETIVO_CON_CAJA
                nueva_grilla[y + my][x + mx] = JUGADOR
                nueva_grilla[y][x] = OBJETIVO
                return nueva_grilla
            else:
                return nueva_grilla
        # ==> caja con objetivo
        elif nueva_grilla[y + my][x + mx] == OBJETIVO_CON_CAJA:
            if nueva_grilla[y + my*2][x + mx*2] == CELDA_VACIA:
                nueva_grilla[y + my*2][x + mx*2] = CAJA
                nueva_grilla[y + my][x + mx] = OBJETIVO_CON_JUGADOR
                nueva_grilla[y][x] = OBJETIVO
                return nueva_grilla
            elif nueva_grilla[y + my*2][x + mx*2] == PARED:
                return nueva_grilla    
            else:
                nueva_grilla[y + my*2][x + mx*2] = OBJETIVO_CON_CAJA
                nueva_grilla[y + my][x + mx] = OBJETIVO_CON_JUGADOR
                nueva_grilla[y][x] = OBJETIVO
                return nueva_grilla
        else:
            return nueva_grilla
    

def encontrar_jugador(grilla):
    ''' busca la posicion del jugador en la grilla '''

    pos_jugador = grilla[0][0]
    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            if grilla[i][j] == JUGADOR or grilla[i][j] == OBJETIVO_CON_JUGADOR:
                pos_jugador = grilla[i][j]
                return i, j

def se_puede_mover(grilla, tupla):
    ''' Esta funcion determina si el jugador puede moverse a la direccion indicada '''

    y, x = encontrar_jugador(grilla)
    mx, my = tupla
    if grilla[y+my][x+mx] == PARED:
        return False
    if grilla[y+my][x+mx] == CELDA_VACIA or grilla[y+my][x+mx] == OBJETIVO:
        return True
    elif grilla[y+my][x+mx] == CAJA or grilla[y+my][x+mx] == OBJETIVO_CON_CAJA:
        if y+my*2 >= len(grilla) or x+mx*2 >= len(grilla[0]):
            return False 
        if grilla[y+my*2][x+mx*2] == CELDA_VACIA or grilla[y+my*2][x+mx*2] == OBJETIVO:
            return True
    return False   