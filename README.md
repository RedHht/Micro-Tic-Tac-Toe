# Micro-Tic-Tac-Toe
##All source files are in the src directory

Tic Tac Toe game for ESP32 made on MicroPython; HTML; CSS & JS

"boot.py" contains the code executed on the boot of the board (Wifi connect, Garbage Collector, etc)

"main.py" contains main code, essentially the code referred to the HTTP request handling and sending info to functions.

"funciones.py" contains majority of the functions referred to checks so the players cant make any trick.

"luces.py" contains code referred to the turn on/off red/green of the lights depending on the movements and wins.

"paginas.py" contains the HTML, CSS & JS code that is sended to the client on a request

Every other file are from the Library/Framework Microdot, that I used to make the handling of the requests and the responses, routes, parameters, etc of the HTTP requests
