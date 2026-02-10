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


from machine import Pin
import time

# --- Pin Assignments ---
SW_PIN  = 20
CLK_PIN = 18
DT_PIN  = 19

btn_pin = Pin(SW_PIN, Pin.IN, Pin.PULL_UP)
clk_pin = Pin(CLK_PIN, Pin.IN, Pin.PULL_UP)
dt_pin  = Pin(DT_PIN,  Pin.IN, Pin.PULL_UP)

prev_clk_value = clk_pin.value()
counter = 0
btn_was_pressed = False

while True:
    curr_clk_value = clk_pin.value()
    btn_curr_state = btn_pin.value()

    # 1. Rotary Encoder Logic
    if curr_clk_value != prev_clk_value:
        if curr_clk_value == 0:    # CLK 1->0
            if dt_pin.value() == 0: # anti-clockwise
                counter -= 1
                dir_label = "<=="
            else:                   # clockwise
                counter += 1
                dir_label = "==>"

            print(dir_label, counter)

        prev_clk_value = curr_clk_value

    # 2. SW Button Logic (Edge Detection)
    # Detect Press (1 -> 0)
    if btn_curr_state == 0 and not btn_was_pressed:
        btn_was_pressed = True
        print("Button: Pressed")

    # Detect Release (0 -> 1)
    elif btn_curr_state == 1 and btn_was_pressed:
        btn_was_pressed = False
        print("Button: Released")

    time.sleep_ms(1)