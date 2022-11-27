import uasyncio
from luces import *

tableroactual = []
ultmov = ""

def rev_mov(movimiento):
    global ultmov
    global tableroactual
    if ultmov == "":
        if movimiento[0] == "R":
            if movimiento in tableroactual or "V" + movimiento[1] in tableroactual:
                print("El jugador rojo se intento mover a una casilla ocupada")
            else:
                moverr(movimiento)
                ultmov = "R"
        elif movimiento[0] == "V":
            print("Movimiento del jugador verde rechazada (Empieza el jugador rojo)")
            pass
    elif ultmov == "R":
        if movimiento[0] == "R":
            print("Movimiento del jugador rojo rechazada (Hizo el ultimo movimiento)")
            pass
        elif movimiento[0] == "V":
            if movimiento in tableroactual or "R" + movimiento[1] in tableroactual:
                print("El jugador rojo se intento mover a una casilla ocupada")
            else:
                moverr(movimiento)
                ultmov = "V"
    elif ultmov == "V":
        if movimiento[0] == "R":
            if movimiento in tableroactual or "V" + movimiento[1] in tableroactual:
                print("El jugador rojo se intento mover a una casilla ocupada")
            else:
                moverr(movimiento)
                ultmov = "R"
        elif movimiento[0] == "V":
            print("Movimiento del jugador verde rechazada (Hizo el ultimo movimiento)")
            pass

def moverr(movimiento):
    tableroactual.append(movimiento)
    prender_pin(movimiento)

def comb_ganadora():
    global tableroactual
    if all(item in tableroactual for item in ["R1", "R2", "R3"]) == True:
        print("Gana el jugador rojo")
        gana_rojo()
        tableroactual = []
    if all(item in tableroactual for item in ["R1", "R4", "R7"]) == True:
        print("Gana el jugador rojo")
        gana_rojo()
        tableroactual = []
    if all(item in tableroactual for item in ["R3", "R6", "R9"]) == True:
        print("Gana el jugador rojo")
        gana_rojo()
        tableroactual = []
    if all(item in tableroactual for item in ["R7", "R8", "R9"]) == True:
        print("Gana el jugador rojo")
        gana_rojo()
        tableroactual = []
    if all(item in tableroactual for item in ["R1", "R5", "R9"]) == True:
        print("Gana el jugador rojo")
        gana_rojo()
        tableroactual = []
    if all(item in tableroactual for item in ["R3", "R5", "R7"]) == True:
        print("Gana el jugador rojo")
        gana_rojo()
        tableroactual = []
    if all(item in tableroactual for item in ["R4", "R5", "R6"]) == True:
        print("Gana el jugador rojo")
        gana_rojo()
        tableroactual = []
    if all(item in tableroactual for item in ["R2", "R5", "R8"]) == True:
        print("Gana el jugador rojo")
        gana_rojo()
        tableroactual = []
    if all(item in tableroactual for item in ["V1", "V2", "V3"]) == True:
        print("Gana el jugador verde")
        gana_verde()
        tableroactual = []
    if all(item in tableroactual for item in ["V1", "V4", "V7"]) == True:
        print("Gana el jugador verde")
        gana_verde()
        tableroactual = []
    if all(item in tableroactual for item in ["V3", "V6", "V9"]) == True:
        print("Gana el jugador verde")
        gana_verde()
        tableroactual = []
    if all(item in tableroactual for item in ["V7", "V8", "V9"]) == True:
        print("Gana el jugador verde")
        gana_verde()
        tableroactual = []
    if all(item in tableroactual for item in ["V1", "V5", "V9"]) == True:
        print("Gana el jugador verde")
        gana_verde()
        tableroactual = []
    if all(item in tableroactual for item in ["V3", "V5", "V7"]) == True:
        print("Gana el jugador verde")
        gana_verde()
        tableroactual = []
    if all(item in tableroactual for item in ["V4", "V5", "V6"]) == True:
        print("Gana el jugador verde")
        gana_verde()
        tableroactual = []
    if all(item in tableroactual for item in ["V2", "V5", "V8"]) == True:
        print("Gana el jugador verde")
        gana_verde()
        tableroactual = []
    
def tablero_lleno():
    global tableroactual
    if len(tableroactual) == 9:
        tableroactual = []
        reiniciar()
