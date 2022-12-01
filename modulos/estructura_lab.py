#----------#1# IMPORTACIONES ----------
from data.lab import muro

#----------#2# VARIABLES ----------
FILAS=5
COLUMNAS=7
#laberinto 'vacío', sólo tiene los huecos, le tenemos que añadir las paredes
mi_laberinto = [ [' ' for c in range(COLUMNAS)] for f in range(FILAS) ] #es un laberinto de 5 filas y 7 columnas


#----------#3# FUNCIONES ----------
def agregar_paredes_lab(laberinto, muro, FILAS, COLUMNAS):
    '''Función que agrega las paredes al laberinto, 
    dada una tupla con las coordenadas en las que están las paredes
    
    -INPUT----------------
    laberinto: lista
        laberinto vacío
    muro: tup
        tupla de coordenadas en las que hay muro
    FILAS: int
        número de filas del laberinto
    COLUMNAS: int
        número de columnas del laberinto
    
    -OUTPUT---------------
    mi_laberinto: list
        laberinto con paredes
    '''
    for f in range(FILAS): #recorremos las filas
        for c in range(COLUMNAS): #recorremos las columnas
            for punto in muro:
                if punto[0]==f and punto[1]==c:
                    laberinto[f][c]='X' #sustituimos el hueco por un muro
                else:
                    pass
    
    return laberinto

def imprimir_laberinto():
    '''Función que imprime el laberinto en pantalla'''
    laberinto = agregar_paredes_lab(mi_laberinto, muro, FILAS, COLUMNAS)

    for f in range(5):
        for c in range(7):
            print(laberinto[f][c],end=' ')
        print()

