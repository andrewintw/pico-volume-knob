# USB HID Boot Keyboard Input Report

* 出現在 USB HID Class Definition 1.11（HID Usage Tables）
* 是 Boot Interface Protocol 的 Keyboard Input Report
* 固定長度 8 bytes，用於 Boot Device（BIOS / OS 開機環境）也能讀鍵盤，不依賴自訂報告描述符


## 8-byte Keyboard Report 結構

| Byte | 名稱        | 說明                                      |
| ---- | --------- | --------------------------------------- |
| 0    | Modifier  | 修飾鍵 (Ctrl / Shift / Alt / GUI) 的 bitmap |
| 1    | Reserved  | 固定 0x00                                 |
| 2    | Keycode 1 | 第一個按鍵的 HID Usage ID                     |
| 3    | Keycode 2 | 第二個按鍵                                   |
| 4    | Keycode 3 | 第三個按鍵                                   |
| 5    | Keycode 4 | 第四個按鍵                                   |
| 6    | Keycode 5 | 第五個按鍵                                   |
| 7    | Keycode 6 | 第六個按鍵                                   |

> USB HID Keyboard report 最多同時可以按 6 個按鍵（除修飾鍵之外）。

## Modifier byte 位元對應（Byte 0）

| Bit | 鍵                        | 說明   |
| --- | ------------------------ | ---- |
| 0   | Left Ctrl                | 0x01 |
| 1   | Left Shift               | 0x02 |
| 2   | Left Alt                 | 0x04 |
| 3   | Left GUI (Windows / Cmd) | 0x08 |
| 4   | Right Ctrl               | 0x10 |
| 5   | Right Shift              | 0x20 |
| 6   | Right Alt                | 0x40 |
| 7   | Right GUI                | 0x80 |


## Keycodes（Bytes 2–7）

| Key       | HID Usage ID |
| --------- | ------------ |
| a         | 0x04         |
| b         | 0x05         |
| c         | 0x06         |
| ...       | ...          |
| 1         | 0x1E         |
| 2         | 0x1F         |
| Enter     | 0x28         |
| Escape    | 0x29         |
| Backspace | 0x2A         |
| Space     | 0x2C         |


* 如果沒有按鍵 → 填 0x00
* 最多 6 個同時按鍵

## 例子：發送大寫 'A'

```
Byte 0: 0x02  ← Left Shift
Byte 1: 0x00  ← Reserved
Byte 2: 0x04  ← 'a'
Byte 3-7: 0x00
```

發送後，再發：

```
Byte 0: 0x00  ← 放開 Shift
Byte 1: 0x00
Byte 2-7: 0x00  ← 放開鍵
```