import gc
gc.collect()

import network
import time
import webrepl

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Conectando al Wi-Fi...')
        sta_if.active(True)
        time.sleep(1)
        sta_if.connect('ASTURIAS', '04082019')
        while not sta_if.isconnected():
            pass
    print('IP Actual:', sta_if.ifconfig()[0])

def crear_ap(essid, password, canal, max_clientes):
    # crea una función que recibe cuatro parámetros: el nombre de la red, la contraseña, el canal y el número máximo de clientes
    ap_if = network.WLAN(network.AP_IF) # instancia el objeto -ap_if- para controlar la interfaz AP
    ap_if.active(True) # activa la interfaz AP
    ap_if.config(essid=essid, password=password, channel=canal, max_clients=max_clientes) # configura los parámetros de la red
    return ap_if # devuelve el objeto -ap_if-



crear_ap("Tic-Tac-Toe", "tecnica32023", 1, 3)
webrepl.start()