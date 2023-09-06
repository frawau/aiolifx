from enum import Enum


class DeviceFeatures(Enum):
    INFO = "Info"
    FIRMWARE = "Firmware"
    WIFI = "Wifi"
    UPTIME = "Uptime"
    POWER = "Power"
    WHITE = "White"
    COLOR = "Color"
    PULSE = "Pulse"
    HEV_CYCLE = "HEV Cycle"
    HEV_CONFIGURATION = "HEV Configuration"
    FIRMWARE_EFFECT = "Firmware Effect"
    FIRMWARE_EFFECT_START_STOP = "Firmware Effect Start/Stop"
    RELAYS = "Relays"
    BUTTONS = "Buttons"
    BUTTON_CONFIG = "Button Config"
    REBOOT = "Reboot"