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
import usb_hid

clk_pin = DigitalInOut(board.GP18)
clk_pin.direction = Direction.INPUT
clk_pin.pull = Pull.UP

dt_pin = DigitalInOut(board.GP19)
dt_pin.direction = Direction.INPUT
dt_pin.pull = Pull.UP

btn = DigitalInOut(board.GP20)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

prev_clk_value = clk_pin.value
counter = 0
btn_was_pressed = False

consumer = next(d for d in usb_hid.devices if d.usage_page == 0x0C) # { 0x0C:consumer, 0x1:keyboard }

# HID Usage ID for Consumer Control
VOLUME_INC = 0xE9
VOLUME_DEC = 0xEA
MUTE = 0xE2

# report = 2-byte little endian
report = bytearray(2)

def send_consumer(usage_id):
    report[0] = usage_id & 0xFF
    report[1] = (usage_id >> 8) & 0xFF
    consumer.send_report(report)
    # Release
    report[0] = 0
    report[1] = 0
    consumer.send_report(report)

while True:
    curr_clk_value = clk_pin.value
    btn_curr_state = btn.value

    # 1. Rotary Encoder Logic
    if curr_clk_value != prev_clk_value:
        if curr_clk_value == 0:    # CLK 1->0
            if dt_pin.value == 0: # anti-clockwise
                send_consumer(VOLUME_DEC)
                counter -= 1
                dir_label = "<=="
            else:                   # clockwise
                send_consumer(VOLUME_INC)
                counter += 1
                dir_label = "==>"

            print(dir_label, counter)

        prev_clk_value = curr_clk_value

    # 2. SW Button Logic (Edge Detection)
    # Detect Press (1 -> 0)
    if btn_curr_state == 0 and not btn_was_pressed:
        send_consumer(MUTE)
        btn_was_pressed = True
        print("Button: Pressed")

    # Detect Release (0 -> 1)
    elif btn_curr_state == 1 and btn_was_pressed:
        btn_was_pressed = False
        print("Button: Released")

    # 運作不太好，有時候轉了半圈，音量才調整一點點。中間有幾個 step 感覺被忽略
    #time.sleep(0.01)    # 但這個移除後，變得比較順耶
