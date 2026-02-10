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
import rotaryio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

encoder = rotaryio.IncrementalEncoder(board.GP18, board.GP19)
cc = ConsumerControl(usb_hid.devices)

btn = DigitalInOut(board.GP20)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

btn_was_pressed = False

last_position = encoder.position

def is_button_pressed(btn_curr_state):
    global btn_was_pressed
    is_pressed = False

    # Detect Press (1 -> 0)
    if btn_curr_state == 0 and not btn_was_pressed:        
        btn_was_pressed = True
        is_pressed = True

    # Detect Release (0 -> 1)
    elif btn_curr_state == 1 and btn_was_pressed:
        btn_was_pressed = False

    return is_pressed

while True:
    position = encoder.position
    if last_position is None or position != last_position:
        #print(position)
        if abs(position) >= 1:
            cc.send(ConsumerControlCode.VOLUME_INCREMENT if position > 0 else ConsumerControlCode.VOLUME_DECREMENT)
            encoder.position = 0
    last_position = position

    if is_button_pressed(btn.value):
        cc.send(ConsumerControlCode.MUTE)
        #print("Button: Pressed")