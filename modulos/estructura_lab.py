#----------#1# IMPORTACIONES ----------
from data.lab import muro

#----------#2# VARIABLES ----------
FILAS=5
COLUMNAS=7

#laberinto 'vacío', sólo tiene los huecos, le tenemos que añadir las paredes
lab_vacio = [ [' ' for c in range(COLUMNAS)] for f in range(FILAS) ] #es un laberinto de 5 filas y 7 columnas


#----------#3# FUNCIONES ----------
def agregar_paredes_lab(lab, paredes, FILAS, COLUMNAS):
    '''Función que agrega las paredes al laberinto, 
    dada una tupla con las coordenadas en las que están las paredes
    
    -INPUT----------------
    lab: lista
        laberinto vacío
    paredes: tup
        tupla de coordenadas en las que hay muro
    FILAS: int
        número de filas del laberinto
    COLUMNAS: int
        número de columnas del laberinto
    
    -OUTPUT---------------
    lab: list
        laberinto con paredes
    '''
    for f in range(FILAS): #recorremos las filas
        for c in range(COLUMNAS): #recorremos las columnas
            for punto in paredes:
                # recorremos las filas y las columnas del laberinto para ir añadiendo pared ('X') 
                # en las coordenadaas que nos indican los puntos de la tupla muro
                if punto[0]==f and punto[1]==c: 
                    lab[f][c]='X' #sustituimos el hueco por un muro
                else:
                    pass
    
    return lab


