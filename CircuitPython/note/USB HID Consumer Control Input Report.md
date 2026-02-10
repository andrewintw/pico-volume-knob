# USB HID Consumer Control Input Report

USB HID Consumer Control Input Report

* 屬於 HID Usage Page 0x0C（Consumer Devices）
* 用於 多媒體 / 音量 / 播放控制 等按鍵
* OS 會把它視作 媒體控制裝置，而不是文字鍵盤

### 報告特性

| 特性             | 說明                                         |
| -------------- | ------------------------------------------ |
| Usage Page     | 0x0C (Consumer Devices)                    |
| Report Type    | Input                                      |
| Report Length  | 通常 2 bytes（16-bit）或 4 bytes 視裝置描述符而定       |
| 每個 bit 或 value | 對應一個 Usage ID，例如 Volume Up、Mute、Play/Pause |
| 按下/放開         | 仍然需要兩個報告：先發 Usage ID，再發 0 表示放開       |


### 常用 Consumer Usage IDs

| 功能             | Usage ID (hex) |
| -------------- | -------------- |
| Volume Up      | 0xE9           |
| Volume Down    | 0xEA           |
| Mute           | 0xE2           |
| Play / Pause   | 0xCD           |
| Next Track     | 0xB5           |
| Previous Track | 0xB6           |


重點：

* Keyboard → Boot Keyboard Input Report (8 bytes)
* Consumer Control → Consumer Control Input Report (通常 2 bytes, HID Page 0x0C)
* 原理一樣：按下 + 放開 → OS 接收 HID report → 執行功能