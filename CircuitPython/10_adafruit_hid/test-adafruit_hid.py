import time
import board
import digitalio

import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

btn = digitalio.DigitalInOut(board.GP20)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

cc = ConsumerControl(usb_hid.devices)

while True:
    btn_state = btn.value

    if btn_state == 0:
        #cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)

        # Debounce/Wait for release
        while btn.value == 0:
            time.sleep(0.01)
            
    time.sleep(0.05)