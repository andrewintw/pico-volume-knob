# Project: Rotary Encoder Button with Status LED
# Hardware: Raspberry Pi Pico + KY-040 + External LED
#
# Wiring Connections:
# -----------------------------------------------------------
# Device       | Pin Name | Pico Pin (GPIO) | Physical Pin
# -------------|----------|-----------------|----------------
# KY-040       | GND      | GND             | Pin 38
# KY-040       | + (VCC)  | 3V3             | Pin 36
# KY-040       | SW       | GP20            | Pin 26
# KY-040       | DT       | GP19            | Pin 25
# KY-040       | CLK      | GP18            | Pin 24
# -------------|----------|-----------------|----------------
# External LED | Anode(+) | GP21            | Pin 27
# External LED | Cathode(-)| GND            | Any GND
# -----------------------------------------------------------

import time
import board
from digitalio import DigitalInOut, Direction, Pull


led = DigitalInOut(board.GP21)
led.direction = Direction.OUTPUT

btn = DigitalInOut(board.GP20)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

while True:
    btn_state = btn.value
    print(int(btn_state), int(led.value))

    if btn_state == 0:
        led.value = not led.value
        
        # Debounce/Wait for release
        while btn.value == 0:
            time.sleep(0.01)
            
    time.sleep(0.05)

