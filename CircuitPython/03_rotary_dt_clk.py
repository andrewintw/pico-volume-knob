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

# clockwise         anti-clockwise
# =============     ==============
# T | CLK | DT      T | CLK | DT
# --|-----|----     --|-----|----
# 0 |  1  | 1       0 |  1  | 1
# 1 |  0  | 1       1 |  1  | 0
# 2 |  0  | 0       2 |  0  | 0
# 3 |  1  | 0       3 |  0  | 1
# 4 |  1  | 1       4 |  1  | 1
# 
# when: CLK 1->0
#   DT=0 => anti-clockwise
#   DT=1 => clockwise
# 
# when: CLK 0->1
#   DT=0 => clockwise
#   DT=1 => anti-clockwise

import time
import board
from digitalio import DigitalInOut, Direction, Pull

clk_pin = DigitalInOut(board.GP18)
clk_pin.direction = Direction.INPUT
clk_pin.pull = Pull.UP

dt_pin = DigitalInOut(board.GP19)
dt_pin.direction = Direction.INPUT
dt_pin.pull = Pull.UP

prev_clk_value = clk_pin.value
counter = 0

while True:
    curr_clk_value = clk_pin.value

    if curr_clk_value != prev_clk_value:
        if curr_clk_value == 0:    # CLK 1->0
            if dt_pin.value == 0: # anti-clockwise
                counter -= 1
                print(counter)
            else:                   # clockwise
                counter += 1
                print(counter)
        prev_clk_value = curr_clk_value

    #time.sleep(0.01)
