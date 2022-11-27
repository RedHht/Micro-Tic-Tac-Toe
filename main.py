from microdot_asyncio import Microdot
from microdot_asyncio_websocket import with_websocket
from machine import WDT
from paginas import rojo, verde
import uasyncio
import time
from luces import *
from funciones import *

iproja = '192.168.50.195'
ipverde = '192.168.50.204'

pinchoto1 = Pin(2, Pin.OUT)
pinchoto2 = Pin(4, Pin.OUT)
#pinchoto3 = Pin(25, Pin.OUT)

pinchoto1.value(1)
pinchoto2.value(1)
#pinchoto3.value(0)

app = Microdot()

@app.route('/')
async def principal(request):
    if request.client_addr[0] == iproja:
        return rojo, 200, {'Content-Type': 'text/html'}
    elif request.client_addr[0] == ipverde:
        return verde, 200, {'Content-Type': 'text/html'}
    else:
        print("Conexion de un jugador rechazada: " + request.client_addr[0])
        return "Conexion no permitida", 405, {'Content-Type': 'text/html'}
    
@app.post('/mover')
async def mover(request):
    if request.client_addr[0] == iproja:
        print("El jugador rojo movio la casilla " + request.args['m'])
        rev_mov('R'+ request.args['m'])
        comb_ganadora()
        tablero_lleno()
    elif request.client_addr[0] == ipverde:
        print("El jugador verde movio la casilla " + request.args['m'])
        rev_mov('V'+ request.args['m'])
        comb_ganadora()
        tablero_lleno()
    else:
        print("Movimiento de un jugador rechazado: " + request.client_addr[0])
        return "Conexion no permitida", 405, {'Content-Type': 'text/html'}
    
@app.route('/socket')
@with_websocket
async def echo(request, ws):
    print("Conexion al websocket recibida")

app.run(debug=True, port=80)