import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300
DIMENSION = 10


def juego_crear():
    """Inicializar el estado del juego"""

    juego = []
    for i in range(DIMENSION):
        juego.append([" " for i in range(DIMENSION)])
    return juego

def juego_actualizar(juego, x, y, nro_turno):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    if x < ANCHO_VENTANA and y < ALTO_VENTANA:   
        celda_x = int(x / (ANCHO_VENTANA / DIMENSION))
        celda_y = int(y / (ALTO_VENTANA / DIMENSION))
        if juego[celda_y][celda_x] == " ":
            juego[celda_y][celda_x] = turno(nro_turno)
            nro_turno += 1
        
    return juego, nro_turno  # devuelve una tupla con el nro_turno para que esta funcion controle el cambio de turno en lugar de main()

def juego_mostrar(juego, nro_turno):
    """Actualizar la ventana"""

    ancho_de_unidad = ANCHO_VENTANA / DIMENSION
    alto_de_unidad = ALTO_VENTANA / DIMENSION
    for i in range(len(juego)):
        for j in range(len(juego[0])):
            gamelib.draw_rectangle(ancho_de_unidad*j, alto_de_unidad*i, ancho_de_unidad*(j+1), alto_de_unidad*(i+1))
    texto_de_turno = f"TURNO: {turno(nro_turno)}"        
    gamelib.draw_text(texto_de_turno, ANCHO_VENTANA / 2, ALTO_VENTANA * 1.1)

    for i in range(len(juego)):
        for j in range(len(juego[0])):
            pos_x_ficha = ancho_de_unidad * j + ancho_de_unidad/2
            pos_y_ficha = alto_de_unidad * i + alto_de_unidad/2
            gamelib.draw_text(juego[i][j], pos_x_ficha, pos_y_ficha, fill="black")

def turno(nro_turno):
    '''Determina el turno'''

    if nro_turno % 2 != 0:
        return "O"
    else:
        return "X"
def main():
    juego = juego_crear()

    nro_turno = 1
    # Ajustar el tamaño de la ventana                       # edité la altura de la ventana para poder mostrar el turno y mantener la grilla simetrica al mismo tiempo
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA*1.2)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego, nro_turno)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego, nro_turno = juego_actualizar(juego, x, y, nro_turno)     # el nuevo nro_turno es el que recibió de juego_actualizar()
gamelib.init(main)