from machine import Pin
from time import sleep

sensor = Pin(1, Pin.IN, Pin.PULL_DOWN)
led = Pin(22, Pin.OUT)

print("now sensing...")

while True:
    if sensor.value() == 0:
        print("sensed something!!")
        led.toggle()
        sleep(1)
    
    sleep(0.001)