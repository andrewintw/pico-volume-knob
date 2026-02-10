import time
import usb_hid

# 8-byte keyboard report
#   Byte 0: Modifier (Ctrl/Shift/Alt/GUI)
#   Byte 1: Reserved (0x00)
#   Byte 2-7: Keycodes (最多 6 個同時按鍵)

KEY_A = 0x04  # HID usage ID for 'a'
report = bytearray(8)
keyboard = usb_hid.devices[0]  # 這個一定要是 Keyboard interface

while True:
    # Press 'A'
    report[0] = 0x02  # Left Shift modifier for uppercase 'A'
    report[2] = KEY_A
    keyboard.send_report(report)

    # Release all keys
    report[0] = 0x00
    report[2] = 0x00
    keyboard.send_report(report)

    time.sleep(0.5)