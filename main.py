from board import Board
from microdot_asyncio import Microdot, Response
from microdot_asyncio_websocket import with_websocket
from microdot_utemplate import render_template
import time
import uasyncio

RED = "R"
GREEN = "G"

app = Microdot()

board = Board()

Response.default_content_type = 'text/html'

@app.get('/')
async def index(request):
    if (request.args['team'] == "R"):
        return render_template('index.html', TEAM="R")
    elif (request.args['team'] == "G"):
        return render_template('index.html', TEAM="G")
    else:
        return "No seleccionaste equipo"
    
@app.post('/move')
async def mover(request):
    board.move(request.args['m'])

@app.route('/ws')
@with_websocket
async def echo(request, ws):
    while True:
        for i in board.websocket_occupied_grids:
            await ws.send(i)

app.run(debug=True, port=80)