from machine import Pin
from microdot_asyncio import Microdot
from microdot_asyncio_websocket import with_websocket
from time import sleep

# Constants

RED = "R"
GREEN = "G"

TEAM = "TEAM"
SLOT = "SLOT"

ON = 0
OFF = 1

LEDS = ({RED: 32, GREEN: 33}, {RED: 25, GREEN: 26}, {RED: 27, GREEN: 14},
        {RED: 23, GREEN: 22}, {RED: 21, GREEN: 19}, {RED: 18, GREEN: 5},
        {RED: 17, GREEN: 16}, {RED: 4, GREEN: 0}, {RED: 2, GREEN: 15})

class Board():
    
    # Logical representation of the occupied spaces by Red/Green or None (Space not occupied) Ex:
    # ["R", "G", "G",
    # None, None, "R"
    # "G", "R", "G"]
    
    occupied_grids = [None, None, None, 
                      None, None, None,
                      None, None, None]
    
    # Physical active pins (The "Pin" objects)
    
    active_leds = []
    
    # ¿Who is going to place a mark this turn? (Red player starts)
    
    turn = RED
    
    # Is a twin of occupied grids, but contains the json format that we are gonna send to the frontend
    
    websocket_occupied_grids = ["", "", "", 
                                "", "", "",
                                "", "", ""]
    
    def __init__(self): # Object constructor, stablish a blank list and turn off some always on pins.
        self.active_leds = []
        
        badpin1 = Pin(23, Pin.OUT)
        badpin2 = Pin(4, Pin.OUT)

        badpin1.value(OFF)
        badpin2.value(OFF)
        
    @staticmethod
    def to_dict_id(id: str) -> tuple:
        
        """ This method splits a relative representation of a Pin (Ex: 'R3', 'G8') into a dict in format (SLOT: int, TEAM: str) """
        
        return {SLOT: int(id[1]), TEAM: id[0]}
        
    @staticmethod 
    def parse_pin(dict_id: dict) -> int:
        
        """ Returns the physical PIN based on a dict_id """
        
        slot = dict_id[SLOT]
        team = dict_id[TEAM]
        
        return LEDS[slot][team]
        
    def update_web_socket_grid(self) -> None:
        
        slot_count = 0
        
        for i in self.occupied_grids:
            color = "red" if i == RED else "green" if i == GREEN else "white"
        
            data = f'''{{
                        "type": "color",
                        "id": "boton{slot_count}",
                        "value": "{color}"
                        }}'''
            
            self.websocket_occupied_grids[slot_count] = (data)
            
            slot_count += 1
        
    def check_for_winners(self) -> str:
        
        """ Check if there is a winner, returns the winner team or None if no one winned """
        
        combinaciones_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        
        for combinacion in combinaciones_ganadoras:
            if self.occupied_grids[combinacion[0]] == self.occupied_grids[combinacion[1]] == self.occupied_grids[combinacion[2]] != None:
                return self.occupied_grids[combinacion[0]]
        return None
    
    def check_turn(self, dict_id: tuple) -> bool:
        
        """ Check if it's the turn of a player, returns True if it's and False if it isn't """
        
        team = dict_id[TEAM]
        
        if (team == self.turn):
            return True
        else:
            return False
        
    def check_occupied(self, dict_id: dict) -> bool:
        
        """ Check if certain slot of the grid is occupied, returns True if it's occupied and False if it isn't """
        
        slot = dict_id[SLOT]
        
        if (self.occupied_grids[slot] is None):
            return False
        else:
            return True
        
    def check_full(self) -> bool:
        
        """ Check if the grid is full, returns True if it's and False if it isn't """
        
        return (None not in self.occupied_grids)
        
    def can_move(self, dict_id: dict) -> bool:
        
        """ Applys all checks and returns True if the move is valid or False if it isn't """
        
        if (not self.check_turn(dict_id)):
            print("No es el turno del jugador")
            return False
        if (self.check_occupied(dict_id)):
            print("La casilla esta ocupada")
            return False
        
        return True
        
    def check_finished(self, dict_id: dict) -> None:
        
        """ Applys all checks about win/reset conditions """
        
        winners_check = self.check_for_winners()
        
        if (winners_check != None):
            self.winner(winners_check)
            self.update_web_socket_grid()
            return False
        
        if (self.check_full()):
            self.reset()
            self.update_web_socket_grid()
            return False
        
    def add_to_grid(self, dict_id: dict) -> None:
        
        """ Adds a value to the grid """
        
        self.occupied_grids[dict_id[SLOT]] = dict_id[TEAM]
        
    def switch_turn(self, dict_id: dict) -> None:
        
        """ Switchs the turn to the other team """
        
        self.turn = GREEN if dict_id[TEAM] == RED else RED
        
    def move(self, id: str) -> None:
        
        """ Activates slots in the grid and makes all checks """
        
        dict_id = Board.to_dict_id(id)
        
        if (self.can_move(dict_id)):
            
            self.add_to_grid(dict_id)
            
            self.update_web_socket_grid()
            
            self.turn_led(dict_id)
            
            self.switch_turn(dict_id)
            
            self.check_finished(dict_id)
            
            
        print(self.occupied_grids)
    
        
    def turn_led(self, dict_id: dict) -> None:
        
        """ Turn on the a physical PIN """
        
        parsed_pin = Pin(Board.parse_pin(dict_id), Pin.OUT)
        
        print("Turning on ", parsed_pin)
        
        parsed_pin.value(ON)
        
        self.active_leds.append(parsed_pin)
        
    def winner(self, winner_team: str) -> None:
        
        """ Win effect, no return """
        
        winner_pins = []
        
        for i in LEDS:
            winner_pins.append(Pin(i[winner_team], Pin.OUT))
            
        for i in range(5):
            for x in winner_pins:
                x.value(ON)
            sleep(0.3)
            for x in winner_pins:
                x.value(OFF)
            sleep(0.3)
            
        self.reset()
            
    def reset(self) -> None:
        
        """ Reset all object values and leds """
        
        self.occupied_grids = [None, None, None, 
                               None, None, None,
                               None, None, None]
        
        for i in self.active_leds:
            i.value(OFF)
        
        self.active_leds = []
        
        self.turn = RED
            
            
        
