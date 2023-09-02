import soko
import gamelib

ANCHO_VENTANA = 1400
ALTO_VENTANA = 800



def cargar_niveles(archivo):
    """ carga los niveles """

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
        c = 0
        while c < len(lista_de_lineas)-1:
            if "Level" in lista_de_lineas[c]:
                c2 = c+1
                lista_de_nivel = []
                while "#" in lista_de_lineas[c2]:
                    lista_de_nivel.append(lista_de_lineas[c2])
                    c2 += 1    
                diccionario_de_niveles[lista_de_lineas[c]] = lista_de_nivel
            c += 1
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
    bloques_de_alto, bloques_de_ancho = dimensiones(grilla)
    ancho_de_unidad = 64
    alto_de_unidad = 64
    
    for i in range(0,20):
        for j in range(0,20):
            gamelib.draw_image("img/ground.gif", i*alto_de_unidad, j*ancho_de_unidad)

    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            if soko.hay_caja(grilla, j, i):
                gamelib.draw_image("img/box.gif",j*alto_de_unidad+64, i*ancho_de_unidad+64)
            if soko.hay_pared(grilla, j, i):
                gamelib.draw_image("img/wall.gif",j*alto_de_unidad+64, i*ancho_de_unidad+64)
            if soko.hay_jugador(grilla, j, i):
                gamelib.draw_image("img/player.gif",j*alto_de_unidad+64, i*ancho_de_unidad+64)
            if soko.hay_objetivo(grilla, j, i):
                gamelib.draw_image("img/goal.gif",j*alto_de_unidad+64, i*ancho_de_unidad+64)

def dimensiones(grilla):
    max_fila = 0
    for i in range(len(grilla)):
        if len(grilla[i]) > max_fila:
            max_fila = len(grilla[i])
    return (max_fila, len(grilla))        


def determinar_direccion(direccion):
    
    if direccion == "NORTE":
        return (0, -1)
    elif direccion == "SUR":
        return (0, 1)
    elif direccion == "ESTE":
        return (1, 0)
    else:
        return (-1, -0)

def main():
    
    diccionario_de_niveles = cargar_niveles("niveles.txt")
    diccionario_de_teclas = cargar_teclas("teclas.txt")
    
    grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles["Level 1"])
    nro_nivel = 1

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
        if diccionario_de_teclas[tecla] == "SALIR":
            break
        elif diccionario_de_teclas[tecla] == "REINICIAR":
            grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles[f"Level {nro_nivel}"])
        elif diccionario_de_teclas[tecla] == "SIGUIENTE":
            nro_nivel += 1
            grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles[f"Level {nro_nivel}"])
        else:
            direccion = determinar_direccion(diccionario_de_teclas[tecla])
            grilla_de_nivel = soko.mover(grilla_de_nivel, direccion)

            if soko.juego_ganado(grilla_de_nivel):
                
                nro_nivel += 1
                grilla_de_nivel = soko.crear_grilla(diccionario_de_niveles[f"Level {nro_nivel}"])
            gamelib.draw_begin()
            dibujar_grilla(grilla_de_nivel)
            gamelib.draw_end()            

gamelib.init(main)
