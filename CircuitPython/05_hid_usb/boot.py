import usb_cdc
import usb_midi
import usb_hid
import storage

# Disable unused features
# usb_cdc.disable()            # REPL/COM port, Thonny cannot connect directly
usb_midi.disable()
# storage.disable_usb_drive()  # CIRCUITPY drive, Windows will not see it

# Enable HID, keep only keyboard
usb_hid.enable((
    usb_hid.Device.KEYBOARD,
))


#  PS C:\MyApps> Get-PnpDevice |
#  >>   Where-Object { $_.InstanceId -match "VID_239A" } |
#  >>   Format-Table Class, FriendlyName, InstanceId
#  
#  Class    FriendlyName                  InstanceId
#  -----    ------------                  ----------
#  Ports    USB 序列裝置 (COM4)           USB\VID_239A&PID_80F4&MI_00\8&10EF392A&0&0000
#  Keyboard HID Keyboard Device           HID\VID_239A&PID_80F4&MI_03\9&DC6A69&0&0000
#  Keyboard HID Keyboard Device           HID\VID_239A&PID_80F4&MI_03&COL01\9&DC6A69&0&0000
#  HIDClass USB 輸入裝置                  USB\VID_239A&PID_80F4\E66044304357AD29
#  USB      USB Mass Storage Device       USB\VID_239A&PID_80F4&MI_02\8&10EF392A&0&0002
#  Mouse    HID-compliant mouse           HID\VID_239A&PID_80F4&MI_03&COL02\9&DC6A69&0&0001
#  HIDClass USB 輸入裝置                  USB\VID_239A&PID_80F4&MI_03\8&10EF392A&0&0003
#  HIDClass 符合 HID 標準的消費者控制裝置 HID\VID_239A&PID_80F4&MI_03&COL03\9&DC6A69&0&0002
#  MEDIA    CircuitPython Audio           USB\VID_239A&PID_80F4&MI_04\8&10EF392A&0&0004
#  Keyboard HID Keyboard Device           HID\VID_239A&PID_80F4\8&10EF392A&0&0000

#  執行後，多了 Keyboard HID Keyboard Device
