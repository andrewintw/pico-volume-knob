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

from machine import Pin
import time

# --- Pin Assignments ---
SW_PIN  = 20
LED_PIN = 21

# --- Initialize Hardware ---
# SW is Active-Low (Pressed = 0, Released = 1)
btn = Pin(SW_PIN, Pin.IN, Pin.PULL_UP)

# LED is Active-High (1 = ON, 0 = OFF)
led = Pin(LED_PIN, Pin.OUT)

print("System Ready. Press the encoder button to toggle LED.")

while True:
    btn_state = btn.value()
    print(btn_state, led.value())

    if btn_state == 0:
        led.toggle()
        
        # Debounce/Wait for release
        while btn.value() == 0:
            time.sleep(0.01)
            
    time.sleep(0.05)