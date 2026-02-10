# [CircuitPython] pi pico 預設的 HID 狀態

```
PS C:\MyApps> Get-PnpDevice -Class HIDClass

Status     Class           FriendlyName                                                                     InstanceId
------     -----           ------------                                                                     ----------
OK         HIDClass        Intel(R) HID Event Filter                                                        ACPI\INTC107...
Unknown    HIDClass        HID-compliant device                                                             HID\VID_2717...
OK         HIDClass        Logitech USB WheelMouse                                                          USB\VID_046D...
OK         HIDClass        符合 HID 標準的廠商定義裝置                                                      HID\VID_258A...
OK         HIDClass        符合 HID 標準的廠商定義裝置                                                      HID\ASUF1204...
OK         HIDClass        USB 輸入裝置                                                                     USB\VID_258A...
OK         HIDClass        符合 HID 標準的系統控制器                                                        HID\VID_258A...
OK         HIDClass        符合 HID 標準的廠商定義裝置                                                      HID\VID_258A...
OK         HIDClass        符合 HID 標準的廠商定義裝置                                                      HID\ASUF1204...
OK         HIDClass        I2C HID 裝置                                                                     ACPI\ASUF120...
Unknown    HIDClass        符合 HID 標準的消費者控制裝置                                                    HID\VID_2717...
OK         HIDClass        符合 HID 標準的消費者控制裝置                                                    HID\VID_258A...
OK         HIDClass        轉換的可攜式裝置控制裝置                                                         BUTTONCONVER...
OK         HIDClass        USB 輸入裝置                                                                     USB\VID_239A...
Unknown    HIDClass        符合 HID 標準的系統控制器                                                        HID\VID_2717...
OK         HIDClass        符合 HID 標準的廠商定義裝置                                                      HID\VID_258A...
OK         HIDClass        符合 HID 標準的廠商定義裝置                                                      HID\VID_258A...
OK         HIDClass        可攜式裝置控制裝置                                                               HID\INTC816\...
OK         HIDClass        ASUS Precision Touchpad                                                          HID\ASUF1204...
OK         HIDClass        符合 HID 標準的消費者控制裝置                                                    HID\CONVERTE...
Unknown    HIDClass        USB 輸入裝置                                                                     USB\VID_2717...
OK         HIDClass        符合 HID 標準的消費者控制裝置                                                    HID\VID_239A...
OK         HIDClass        I2C HID 裝置                                                                     ACPI\ITE5570\1
Unknown    HIDClass        HID-compliant device                                                             HID\VID_2717...
OK         HIDClass        符合 HID 標準的無線通訊裝置控制項                                                HID\ITE5570\...
OK         HIDClass        Microsoft Input Configuration Device                                             HID\ASUF1204...
OK         HIDClass        符合 HID 標準的系統控制器                                                        HID\CONVERTE...
OK         HIDClass        USB 輸入裝置                                                                     USB\VID_258A...
```

CircuitPython / Adafruit Pico 通常是：VID_239A

```
PS C:\MyApps> Get-PnpDevice -Class HIDClass |
>>   Where-Object { $_.InstanceId -match "VID_239A" } |
>>   Format-List Status, FriendlyName, InstanceId
```

輸出兩個:

節點 1

```
Status       : OK
FriendlyName : USB 輸入裝置
InstanceId   : USB\VID_239A&PID_80F4&MI_03\8&10EF392A&0&0003
```

解讀：

* VID_239A → Adafruit / CircuitPython
* PID_80F4 → Pico 對應的 CircuitPython PID
* MI_03 → 第 3 個 USB interface
* USB\... → 這是 USB interface 層級的裝置節點

這通常是 Composite Device 的 interface

節點 2

```
Status       : OK
FriendlyName : 符合 HID 標準的消費者控制裝置
InstanceId   : HID\VID_239A&PID_80F4&MI_03&COL03\9&DC6A69&0&0002
```

解讀：

* 這是 HID Consumer Control
* 用來送：
	- 音量 +
	- 音量 –
	- 播放 / 暫停
* COL03 → HID collection 3
* 它是從上一個 USB interface 延伸出來的 HID child device


```
PS C:\MyApps> Get-PnpDevice |
>>   Where-Object { $_.InstanceId -match "VID_239A" } |
>>   Format-Table Class, FriendlyName, InstanceId

Class    FriendlyName                  InstanceId
-----    ------------                  ----------
Ports    USB 序列裝置 (COM4)            USB\VID_239A&PID_80F4&MI_00\8&10EF392A&0&0000
Keyboard HID Keyboard Device           HID\VID_239A&PID_80F4&MI_03\9&DC6A69&0&0000
Keyboard HID Keyboard Device           HID\VID_239A&PID_80F4&MI_03&COL01\9&DC6A69&0&0000
USB      USB Composite Device          USB\VID_239A&PID_80F4\E66044304357AD29
USB      USB Mass Storage Device       USB\VID_239A&PID_80F4&MI_02\8&10EF392A&0&0002
Mouse    HID-compliant mouse           HID\VID_239A&PID_80F4&MI_03&COL02\9&DC6A69&0&0001
HIDClass USB 輸入裝置                   USB\VID_239A&PID_80F4&MI_03\8&10EF392A&0&0003
HIDClass 符合 HID 標準的消費者控制裝置    HID\VID_239A&PID_80F4&MI_03&COL03\9&DC6A69&0&0002
MEDIA    CircuitPython Audio           USB\VID_239A&PID_80F4&MI_04\8&10EF392A&0&0004
```

你現在的 Pico 對 Win11 來說是：

> 「鍵盤 + 滑鼠 + 音量鍵 + 音效卡 + 隨身碟 + COM port」

### 父節點（實體 Pico）

```
USB Composite Device
USB\VID_239A&PID_80F4\E66044304357AD29
```

這行 = Pico 本體


### MI_00 — USB CDC（序列埠）

```
Ports
USB 序列裝置 (COM4)
USB\VID_239A&PID_80F4&MI_00\...
```

* CircuitPython 的 REPL / log
* 這是「功能之一」


### MI_02 — USB Mass Storage

```
USB
USB Mass Storage Device
USB\VID_239A&PID_80F4&MI_02\...
```

* CIRCUITPY
* 用來拖檔案


### MI_03 — USB HID（複合）

```
HIDClass USB 輸入裝置
HID\VID_239A&PID_80F4&MI_03\...
```

這是一個 HID interface，底下再拆成多個 HID Collections：

| HID Collection | Windows 顯示          | 用途         |
| -------------- | ------------------- | ---------- |
| COL01          | HID Keyboard Device | 鍵盤         |
| COL02          | HID-compliant mouse | 滑鼠         |
| COL03          | 符合 HID 標準的消費者控制裝置   | 音量鍵 / 多媒體鍵 |

不是三個裝置，是同一個 HID interface 的三個 collection



### MI_04 — USB Audio

```
MEDIA
CircuitPython Audio
USB\VID_239A&PID_80F4&MI_04\...
```

* CircuitPython 的 USB Audio
* 又是一個獨立 interface


