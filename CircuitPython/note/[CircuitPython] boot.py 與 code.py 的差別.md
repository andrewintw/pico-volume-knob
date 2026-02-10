# [CircuitPython] boot.py 與 code.py 的差別

### boot.py 與 code.py 的差別

| 檔案                    | 執行時機                     | 影響                                                                                          |
| --------------------- | ------------------------ | ------------------------------------------------------------------------------------------- |
| **boot.py**           | Pico 上電 / reset **最先執行** | 可以決定 USB descriptor / Composite Device 啟用哪些功能<br>影響 Windows 看到的裝置（CIRCUITPY、COM port、HID 等） |
| **code.py / main.py** | boot.py 執行完後執行           | 只能操作已經存在的 USB interface<br>對 Windows 看到的裝置「已經被初始化」後才會改變，某些功能（像 storage）可能無法正確 disable       |


```
import usb_cdc
import usb_midi
import usb_hid
import usb_audio
import storage

# Disable unused features
usb_cdc.disable()            # REPL/COM port, Thonny cannot connect directly
usb_midi.disable()
usb_audio.disable()
storage.disable_usb_drive()  # CIRCUITPY drive, Windows will not see it

# Enable HID, keep only keyboard
usb_hid.enable((
    usb_hid.Device.KEYBOARD,
))
```

### 如果把你那段放在 code.py 會發生什麼事

* usb_hid.enable(KEYBOARD) → 可以執行，鍵盤還是能用
* storage.disable_usb_drive() → 可能無效，因為 CIRCUITPY 已經被 Windows mount 成磁碟了
* usb_cdc.disable() → Thonny REPL 可能還是會先顯示 COM port，Windows 可能不會立刻移除
* Windows 裝置管理員可能還會短暫看到 COM port / Mass Storage / Mouse 等
* 重置後立即顯示的裝置狀態 無法被改變，因為 boot.py 先跑過了

簡單說：

> 放在 code.py 是「後手控制」，Windows 看到的 USB 裝置可能還是會有短暫存在的 COM / Mass Storage / Mouse，對你想做「最小鍵盤 HID only」的目標不夠乾淨。


### 建議

* 要乾淨只保留鍵盤 → 放在 boot.py
* 只是程式邏輯控制 / HID 發送資料 → 放在 code.py
* 可以這樣分工：
	- `boot.py` → USB descriptor / enable/disable
	- `code.py` → 讀旋轉編碼器、送按鍵報告

