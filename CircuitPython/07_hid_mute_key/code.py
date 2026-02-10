import time
import usb_hid
import digitalio
import board

btn = digitalio.DigitalInOut(board.GP20)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

keyboard = usb_hid.devices[0]  # 這個一定要是 Keyboard interface
consumer = usb_hid.devices[1]

MUTE = 0xE2  # HID Usage ID for Mute

# 2-byte report
report = bytearray(2)

last_state = True # Button Released

print("keyboard.usage_page:", hex(keyboard.usage_page)) # 0x1
print("consumer.usage_page:", hex(consumer.usage_page)) # 0xC

while True:
    btn_pressed = not btn.value

    if btn_pressed and last_state:
        last_state = False
  
        # Button pressed → 發送 Mute
        report[0] = MUTE & 0xFF
        report[1] = (MUTE >> 8) & 0xFF
        consumer.send_report(report)

        # Release
        report[0] = 0x00
        report[1] = 0x00
        consumer.send_report(report)

        print("Button: Pressed")
        time.sleep(0.05)  # simple debounce

    elif not btn_pressed and not last_state:
        last_state = True
        print("Button: Released")
    
    time.sleep(0.01)