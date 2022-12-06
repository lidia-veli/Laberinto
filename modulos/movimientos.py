#  ---------- #1 IMPORTACIONES ----------
from data.lab import muro
from modulos.estructura_lab import (
    agregar_paredes_lab,
    FILAS,
    COLUMNAS,
    lab_vacio
)

# ---------- #2 VARIABLES ----------
#laberinto con las paredes dadas por la tupla muro
laberinto = agregar_paredes_lab(lab_vacio, muro, FILAS, COLUMNAS) 

path = [] # lista donde vamos a guardar los movimientos que haga el jugador

# ---------- #3 FUNCIONES ----------

def entrada_lab(lab):
    '''Función que pone al jugador en la entrada del laberinto
    -INPUT----------------
    laberinto: list
        laberinto con paredes
    -OUTPUT---------------
    laberinto: list
        laberinto con el jugador colocado en la entrada
    '''
    for c in range(COLUMNAS):
        if lab[0][c] == ' ': #si hay un hueco
            lab[0][c] = 'o' # nos ponemos en la entrada
            break #si hay más de un hueco, nosponemos en el primero que encuentre
    
    return lab


def moverse_una_casilla(lab, path):
    '''Función que mueve al jugador una casilla donde haya un hueco
    -INPUT----------------
    lab: list
        laberinto con el jugador
    path: list
        lista de movimientos que ha hecho el jugador
    -OUTPUT---------------
    (lab, path): tup
        lab: list
            laberinto con el jugador movido
        path: list
            lista actualizada de movimientos que ha hecho el jugador'''
    
    for f in range(FILAS): # recorremos las filas
        for c in range(COLUMNAS): # y las columnas
            
            if lab[f][c]=='o': #si el jugador está en esa (f,c)
                
                # si hay un hueco debajo (fila+1, misma columna)
                if lab[f+1][c]==' ': 
                    lab[f+1][c]='o' # nos movemos al hueco
                    lab[f][c]=' ' # y la casilla en la que estabamos la dejamos vacía
                    path.append('abajo') #guardamos nuestro movimiento
                    return lab , path
                
                #si hay un hueco encima (fila-1, misma columna)
                elif lab[f-1][c]==' ':
                    lab[f-1][c]='o' # nos movemos al hueco
                    lab[f][c]=' ' #y la casilla en la que estabamos la dejamos vacía
                    path.append('arriba') #guardamos nuestro movimiento
                    return lab , path
                
                # si hay un hueco a la derecha (misma fila, columna+1)
                if lab[f][c+1]==' ': 
                    lab[f][c+1]='o' # nos movemos al hueco
                    lab[f][c]=' ' #y la casilla en la que estabamos la dejamos vacía
                    path.append('derecha') #guardamos nuestro movimiento
                    return lab , path
                
                #si hay un hueco a la izquierda (misma fila, columna-1)
                elif lab[f][c-1]==' ':
                    lab[f][c-1]='o' # nos movemos al hueco
                    lab[f][c]=' ' #y la casilla en la que estabamos la dejamos vacía
                    path.append('izquierda') #guardamos nuestro movimiento
                    return lab , path
            
            else: #si el jugador no está en esa (f,c), seguimos recorriendo las posiciones
                pass


