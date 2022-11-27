from machine import Pin, PWM
import machine
import time

pwms = []
pines = []

#Definicion de pines

R1 = 32
V1 = 33
R2 = 25
V2 = 26
R3 = 27
V3 = 14
R4 = 23
V4 = 22
R5 = 21
V5 = 19
R6 = 18
V6 = 5
R7 = 17
V7 = 16
R8 = 4
V8 = 0
R9 = 2
V9 = 15

f = 1000#Hz

def prender_pin(id):
    #pwms.append(PWM(Pin(globals()[id]), freq= f * (len(pwms) // 2 + 1), duty=1))
    pines.append(Pin(globals()[id], Pin.OUT))
    pines[pines.index(Pin(globals()[id], Pin.OUT))].value(0)
    print("Se prendio el PIN", globals()[id])
    print(pwms)

    
def gana_rojo():
    gana_rojo_luces = []
    reiniciar()
    contador = 0
    while contador <= 3:
        luces = 1
        while luces <= 9:
            gana_rojo_luces.append(Pin(globals()["R" + str(luces)], Pin.OUT))
            luces += 1
        for i in gana_rojo_luces:
            i.value(0)
        time.sleep(0.3)
        for x in gana_rojo_luces:
            x.value(1)
        time.sleep(0.3)
        contador += 1
        
def gana_verde():
    gana_rojo_luces = []
    reiniciar()
    contador = 0
    while contador <= 3:
        luces = 1
        while luces <= 9:
            gana_rojo_luces.append(Pin(globals()["V" + str(luces)], Pin.OUT))
            luces += 1
        for i in gana_rojo_luces:
            i.value(0)
        time.sleep(0.3)
        for x in gana_rojo_luces:
            x.value(1)
        time.sleep(0.3)
        contador += 1
    
def reiniciar():
    global pwms
    global pines
    time.sleep(1)
    for x in pines:
        x.value(1)
    print(pwms)
    pines = []
    pwms = []
    tableroactual = []


