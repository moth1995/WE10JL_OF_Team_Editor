import os
import sys
from tkinter import messagebox

def bytes_to_int(ba, a):
    ia = [ba[a + i] for i in range(4)]
    return ia[0] | (ia[1] << 8) | (ia[2] << 16) | (ia[3] << 24)

def zero_fill_right_shift(val, n):
    return (val % 0x100000000) >> n

def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return value

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return [int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def report_callback_exception(self, exc, val, tb):
    messagebox.showerror("Error", message=str(val))
