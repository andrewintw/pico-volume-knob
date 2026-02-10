# import usb_cdc
import usb_midi
import usb_hid
# import storage

# Disable unused features
# usb_cdc.disable()            # REPL/COM port, Thonny cannot connect directly
usb_midi.disable()
# storage.disable_usb_drive()  # CIRCUITPY drive, Windows will not see it

# Enable HID, keep only keyboard
usb_hid.enable((
    usb_hid.Device.KEYBOARD,
    usb_hid.Device.MOUSE,
    usb_hid.Device.CONSUMER_CONTROL,
))