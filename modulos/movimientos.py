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


def moverse_a_casilla_no_pisada(lab, path, mov):
    '''Función que mueve al jugador una casilla donde haya un hueco y por donde no haya pasado antes
    
    -INPUT----------------
    lab: list
        laberinto con el jugador
    path: list
        lista con las coordenadas de las casillas por las que ya ha pasado el jugador
    mov: list
        lista con los movimientos que va haciendo el jugador
    
    -OUTPUT----------------
    lab: list
        laberinto con el jugador movido
    path: list
        lista actualizada con las coordenadas de las casillas por las que ya ha pasado el jugador
    mov: list
        lista actualizada con los movimientos que va haciendo el jugador
    '''
    for f in range(FILAS): # recorremos las filas
            for c in range(COLUMNAS): # y las columnas
                
                if lab[f][c]=='o': #si el jugador está en esa (f,c)
                    path.append( (f,c) ) #guardamos las coordenadas de la casilla en la que estamos (pisada)
                    
                    # si hay un hueco a la derecha (misma fila, columna+1) y es una casilla no pisada anteriormente
                    if lab[f][c+1]==' ' and (f,c+1) not in path: 
                        lab[f][c+1]='o' # nos movemos al hueco
                        lab[f][c]=' ' #y la casilla en la que estabamos la dejamos vacía
                        mov.append('derecha') #guardamos nuestro movimiento
                        return lab , path, mov
                    
                    # si hay un hueco a la izquierda (misma fila, columna-1) y es una casilla no pisada anteriormente
                    if lab[f][c-1]==' ' and (f,c-1) not in path: 
                        lab[f][c-1]='o' # nos movemos al hueco
                        lab[f][c]=' ' #y la casilla en la que estabamos la dejamos vacía
                        mov.append('izquierda') #guardamos nuestro movimiento
                        return lab , path, mov
                    
                    # si hay un hueco debajo (fila+1, misma columna) y es una casilla no pisada anteriormente
                    elif lab[f+1][c]==' ' and (f+1,c) not in path:
                        lab[f+1][c]='o' # nos movemos al hueco
                        lab[f][c]=' ' # y la casilla en la que estabamos la dejamos vacía
                        mov.append('abajo') #guardamos nuestro movimiento
                        return lab , path, mov
                
                    #si hay un hueco encima (fila-1, misma columna) y es una casilla no pisada anteriormente
                    elif lab[f-1][c]==' ' and (f-1,c) not in path:
                        lab[f-1][c]='o' # nos movemos al hueco
                        lab[f][c]=' ' #y la casilla en la que estabamos la dejamos vacía
                        mov.append('arriba') #guardamos nuestro movimiento
                        return lab , path, mov
                
                else: #si no está el jugador en esa casilla, segimos recorriendo coordenadas
                    pass


