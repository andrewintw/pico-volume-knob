import time
import usb_hid

# HID Usage ID 對照表（常用）
KEY_A = 0x04
KEY_B = 0x05
KEY_C = 0x06
KEY_D = 0x07
KEY_E = 0x08
KEY_F = 0x09
KEY_G = 0x0A
KEY_H = 0x0B
KEY_I = 0x0C
KEY_J = 0x0D
KEY_K = 0x0E
KEY_L = 0x0F
KEY_M = 0x10
KEY_N = 0x11
KEY_O = 0x12
KEY_P = 0x13
KEY_Q = 0x14
KEY_R = 0x15
KEY_S = 0x16
KEY_T = 0x17
KEY_U = 0x18
KEY_V = 0x19
KEY_W = 0x1A
KEY_X = 0x1B
KEY_Y = 0x1C
KEY_Z = 0x1D
KEY_1 = 0x1E
KEY_2 = 0x1F
KEY_3 = 0x20
KEY_4 = 0x21
KEY_5 = 0x22
KEY_6 = 0x23
KEY_7 = 0x24
KEY_8 = 0x25
KEY_9 = 0x26
KEY_0 = 0x27
KEY_ENTER = 0x28
KEY_ESC = 0x29
KEY_BACKSPACE = 0x2A
KEY_TAB = 0x2B
KEY_SPACE = 0x2C
KEY_MINUS = 0x2D
KEY_EQUAL = 0x2E

# 8-byte report
report = bytearray(8)
keyboard = usb_hid.devices[0]  # 必須是 Keyboard interface

# 字符對應 HID 用法與是否要 Shift
char_map = {
    "a": (KEY_A, False), "b": (KEY_B, False), "c": (KEY_C, False), "d": (KEY_D, False),
    "e": (KEY_E, False), "f": (KEY_F, False), "g": (KEY_G, False), "h": (KEY_H, False),
    "i": (KEY_I, False), "j": (KEY_J, False), "k": (KEY_K, False), "l": (KEY_L, False),
    "m": (KEY_M, False), "n": (KEY_N, False), "o": (KEY_O, False), "p": (KEY_P, False),
    "q": (KEY_Q, False), "r": (KEY_R, False), "s": (KEY_S, False), "t": (KEY_T, False),
    "u": (KEY_U, False), "v": (KEY_V, False), "w": (KEY_W, False), "x": (KEY_X, False),
    "y": (KEY_Y, False), "z": (KEY_Z, False),
    "A": (KEY_A, True), "B": (KEY_B, True), "C": (KEY_C, True), "D": (KEY_D, True),
    "E": (KEY_E, True), "F": (KEY_F, True), "G": (KEY_G, True), "H": (KEY_H, True),
    "I": (KEY_I, True), "J": (KEY_J, True), "K": (KEY_K, True), "L": (KEY_L, True),
    "M": (KEY_M, True), "N": (KEY_N, True), "O": (KEY_O, True), "P": (KEY_P, True),
    "Q": (KEY_Q, True), "R": (KEY_R, True), "S": (KEY_S, True), "T": (KEY_T, True),
    "U": (KEY_U, True), "V": (KEY_V, True), "W": (KEY_W, True), "X": (KEY_X, True),
    "Y": (KEY_Y, True), "Z": (KEY_Z, True),
    " ": (KEY_SPACE, False),
    "-": (KEY_MINUS, False),
    "x": (KEY_X, False),
}

def send_char(c):
    key, shift = char_map[c]
    # Press
    report[0] = 0x02 if shift else 0x00
    report[2] = key
    keyboard.send_report(report)
    # Release
    report[0] = 0x00
    report[2] = 0x00
    keyboard.send_report(report)
    time.sleep(0.02)  # 避免漏鍵


time.sleep(5)

text = "Tzu-Tung x Andrew"
for ch in text:
    send_char(ch)
