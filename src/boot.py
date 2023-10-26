import webrepl

def conectar_wifi():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Conectando al Wi-Fi...')
        sta_if.active(True)
        sta_if.connect('Red Mesh', 'Thiago010805')
        while not sta_if.isconnected():
            pass
    print('IP Actual:', sta_if.ifconfig()[0])

def crear_wifi():
    import network
    ap = network.WLAN(network.AP_IF)
    ap.config(ssid='ESP-AP')
    ap.config(max_clients=10)
    ap.active(True)
conectar_wifi()
webrepl.start()
