import time
import usb_hid
import digitalio
import board

btn = digitalio.DigitalInOut(board.GP20)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

# keyboard = usb_hid.devices[0]
# consumer = usb_hid.devices[1]
consumer = next(d for d in usb_hid.devices if d.usage_page == 0x0C)

MUTE = 0xE2  # HID Usage ID for Mute

# 2-byte report
report = bytearray(2)

button_released  = True # Button Released

def send_consumer(usage_id):
    report[0] = usage_id & 0xFF
    report[1] = (usage_id >> 8) & 0xFF
    consumer.send_report(report)
    # Release
    report[0] = 0
    report[1] = 0
    consumer.send_report(report)


while True:
    btn_pressed = not btn.value

    if btn_pressed  and button_released:
        button_released  = False
        send_consumer(MUTE)
        print("Button: Pressed")
        time.sleep(0.05)  # simple debounce

    elif not btn_pressed  and not button_released :
        button_released  = True
        print("Button: Released")
    
    time.sleep(0.01)
