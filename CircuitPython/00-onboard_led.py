"""Example for Pico. Turns on the built-in LED."""
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
#led = digitalio.DigitalInOut(board.GP21)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(0.3)