from machine import Pin
import time


def blink():
    led = Pin(Pin.board.LED, Pin.OUT)
    led.toggle()

    print(f"{time.time_ns()}: blink {led.value()}!")
    time.sleep(0.5)
