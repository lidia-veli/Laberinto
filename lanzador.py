#----------#1# IMPORTACIONES ----------
from modulos.estructura_lab import FILAS, COLUMNAS

from modulos.movimientos import (
    entrada_lab,
    moverse_a_casilla_no_pisada,
    laberinto,
    )

#----------#2# VARIABLES ----------


#----------#3# FUNCIONES ----------

def imprimir_laberinto(lab):
    '''Función que imprime el laberinto en pantalla'''
    for f in range(FILAS):
        for c in range(COLUMNAS):
            print(lab[f][c],end=' ')
        print()


def escapar_laberinto():
    '''Función que simula el movimiento del jugador en el laberinto'''

    print('Laberinto inicial:')
    laberinto_ent = entrada_lab(laberinto) #jugador e la entrada del laberinto
    imprimir_laberinto(laberinto_ent)
    print( )
    path = [ (0,1) ] #casillas que ya hemos pisado: la entrada del laberinto
    mov = [] #lista vacía en la que guardaremos los movimientos que hagamos

    #movemos al jugador a una casilla no pisada
    lab_mov = moverse_a_casilla_no_pisada(laberinto_ent, path, mov) #3-tupla (lab, path, mov)
    contador = 1

    #BUCLE para seguir moviendonos, mientras no estemos en la salida del laberinto
    while lab_mov[0][-1][-2] != 'o': 
                # casilla SALIDA: última fila, penúltima columna
        lab_mov = moverse_a_casilla_no_pisada(lab_mov[0], lab_mov[1], lab_mov[2]) #3-tupla (lab, path, mov)
        contador += 1

    print('El jugador ha necesitado', contador, 'movimientos para salir del laberinto.')
    print('Estos son los movimientos del jugador:')
    print(lab_mov[2]) # lista de movimientos
