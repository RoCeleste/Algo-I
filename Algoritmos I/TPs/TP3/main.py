import soko
import gamelib
import pila
import cola

NORTE = (0, -1)
SUR = (0, 1)
ESTE = (1, 0)
OESTE = (-1, 0)

TECLAS = "teclas.txt"
NIVELES = "niveles.txt"

IMAGEN_CAJA = "img/box.gif"
IMAGEN_JUGADOR = "img/player.gif"
IMAGEN_PARED = "img/wall.gif"
IMAGEN_PISO = "img/ground.gif"
IMAGEN_OBJETIVO = "img/goal.gif"


ANCHO_VENTANA = 1400
ALTO_VENTANA = 900

def cargar_niveles(archivo):
    """ carga los niveles """
    llave = 1                                   #las llaves del diccionario ahora son enteros en lugar de cadenas
    diccionario_de_niveles = {}
    lista_de_lineas = []
    try:
        with open(archivo, "r") as niveles:
            for linea in niveles:
                linea = linea.rstrip()
                lista_de_lineas.append(linea)
    except:
        raise Exception("No existe el archivo")
    try:
        c = 0                                           #c es la linea actual
        while c < len(lista_de_lineas)-1:
            if "Level" in lista_de_lineas[c]:
                c2 = c+1                                #c2 es la linea siguiente
                lista_de_nivel = []
                while "#" in lista_de_lineas[c2]:                       #mientras la linea sea parte de la grilla,
                    lista_de_nivel.append(lista_de_lineas[c2])
                    c2 += 1                                             #la agregamos y avanzamos hasta encontrar una linea vacia (que no forma parte de la grilla)
                diccionario_de_niveles[llave] = lista_de_nivel          
                llave += 1
            c += 1                                                      #avanzamos c hasta la siguiente grilla
    except IndexError:
        raise IndexError("Hay que agregar un caracter no nulo a la ultima linea")

    return diccionario_de_niveles     
                

def cargar_teclas(archivo):
    """ carga las teclas """

    teclas = {}
    with open(archivo, "r") as archivo_de_teclas:
        for linea in archivo_de_teclas:
            linea = linea.strip()
            lista_temp = linea.split(",")
            teclas[lista_temp[0]] = lista_temp[1]
    return teclas

def dibujar_grilla(grilla):
    """ dibuja la grilla """
    ancho_de_unidad = 64        
    alto_de_unidad = 64         
    
    for i in range(0,24):
        for j in range(0,20):
            gamelib.draw_image(IMAGEN_PISO, i*alto_de_unidad, j*ancho_de_unidad)    #pinta el piso en toda la pantalla, aunque exceda la grilla
                                                                                    #esto es para que no queden partes negras en la pantalla
    
    for i in range(len(grilla)):
        
        for j in range(len(grilla[i])):                                                     #pinta los bloques de acuerdo a la grilla
            if soko.hay_caja(grilla, j, i):
                gamelib.draw_image(IMAGEN_CAJA,j*alto_de_unidad, i*ancho_de_unidad)
            if soko.hay_pared(grilla, j, i):
                gamelib.draw_image(IMAGEN_PARED,j*alto_de_unidad, i*ancho_de_unidad)
            if soko.hay_jugador(grilla, j, i):
                gamelib.draw_image(IMAGEN_JUGADOR,j*alto_de_unidad, i*ancho_de_unidad)
            if soko.hay_objetivo(grilla, j, i):
                gamelib.draw_image(IMAGEN_OBJETIVO,j*alto_de_unidad, i*ancho_de_unidad)


def determinar_direccion(direccion):
    
    if direccion == "NORTE":
        return NORTE
    elif direccion == "SUR":
        return SUR
    elif direccion == "ESTE":
        return ESTE
    elif direccion == "OESTE":
        return OESTE

def buscar_solucion(grilla):
    grillas_visitadas = []
    return backtrack(grilla, grillas_visitadas)

def concatenar_diccionario(dic1, dic2):
    for llave in dic2:
        dic1[llave] = dic2[llave]
    return dic1    


def h(grilla_de_nivel):
    '''hace inmutable la lista de niveles al convertirlo en una cadena en el formato niveles.txt'''
    resultado = ""
    for fila in grilla_de_nivel:
        cadena = "".join(fila)
        resultado += cadena + "\n"
    return resultado

def backtrack(grilla, grillas_visitadas):

    grillas_visitadas.append(grilla)
    if soko.juego_ganado(grilla):
        return True, []
    for direccion in [NORTE, OESTE, ESTE, SUR]:       
        grilla_resultante = soko.mover(grilla, direccion)
        if grilla_resultante in grillas_visitadas:
            continue
        solucion, grillas_acciones = backtrack(grilla_resultante, grillas_visitadas)
        if solucion:
            return True, [direccion] + grillas_acciones
    return False, None

def actualizar_grilla(grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas):
    if accion == "REINICIAR":

        while not pila_anteriores.esta_vacia():     #reiniciamos las pilas
            pila_anteriores.desapilar()
        while not pila_posteriores.esta_vacia():
            pila_posteriores.desapilar()

        grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles[nro_nivel])
        return grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas

    elif accion == "SIGUIENTE":
        
        while not pila_anteriores.esta_vacia():     #reiniciamos las pilas
            pila_anteriores.desapilar()
        while not pila_posteriores.esta_vacia():
            pila_posteriores.desapilar()

        nro_nivel += 1
        if nro_nivel == len(diccionario_de_niveles):
            raise Exception("llegaste al ultimo nivel")
        grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles[nro_nivel])
        return grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas

    elif accion == "DESHACER":
        if not pila_anteriores.esta_vacia():
            pila_posteriores.apilar(grilla_de_nivel)
            grilla_de_nivel = pila_anteriores.desapilar()
        return grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas


    elif accion == "REHACER":
        if not pila_posteriores.esta_vacia():
            pila_anteriores.apilar(grilla_de_nivel)
            grilla_de_nivel = pila_posteriores.desapilar()
        return grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas

    elif accion == "PISTA":

        if len(lista_de_pistas) == 0:
            lista_de_pistas = buscar_solucion(grilla_de_nivel)[1]
            print(lista_de_pistas)
            grilla_de_nivel = soko.mover(grilla_de_nivel, lista_de_pistas.pop(0))
            return grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas

        else:
            grilla_de_nivel = soko.mover(grilla_de_nivel, lista_de_pistas.pop(0))

            if soko.juego_ganado(grilla_de_nivel):
                lista_de_pistas = []
                while not pila_anteriores.esta_vacia():     #reiniciamos las pilas
                    pila_anteriores.desapilar()
                while not pila_posteriores.esta_vacia():
                    pila_posteriores.desapilar()

                nro_nivel += 1
                if nro_nivel == len(diccionario_de_niveles):
                    raise Exception("llegaste al ultimo nivel")
                grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles[nro_nivel])


            return grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas

    else:
        pila_anteriores.apilar(grilla_de_nivel)
        direccion = determinar_direccion(accion)
        grilla_de_nivel = soko.mover(grilla_de_nivel, direccion)

        if soko.juego_ganado(grilla_de_nivel):
            while not pila_anteriores.esta_vacia():     #reiniciamos las pilas
                pila_anteriores.desapilar()
            while not pila_posteriores.esta_vacia():
                pila_posteriores.desapilar()

            nro_nivel += 1
            if nro_nivel == len(diccionario_de_niveles):
                raise Exception("llegaste al ultimo nivel")
            grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles[nro_nivel])
        return grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas



def main():
    
    try:
        diccionario_de_niveles = cargar_niveles(NIVELES)
        diccionario_de_teclas = cargar_teclas(TECLAS)
    except:
        raise Exception("No existe alguno de los archivos")    

    grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles[1])
    nro_nivel = 1

    pila_anteriores = pila.Pila()
    pila_posteriores = pila.Pila()
    lista_de_pistas = []

    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():
        gamelib.draw_begin()
        dibujar_grilla(grilla_de_nivel)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        # Actualizar el estado del juego, según la `tecla` presionada
        if tecla in diccionario_de_teclas:
            accion = diccionario_de_teclas[tecla]
            if accion == "SALIR":
                break
            grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas = actualizar_grilla(grilla_de_nivel, accion, diccionario_de_niveles, nro_nivel, pila_anteriores, pila_posteriores, lista_de_pistas)            

gamelib.init(main)
