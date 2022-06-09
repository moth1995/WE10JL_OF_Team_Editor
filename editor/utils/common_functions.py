import os
from string import ascii_uppercase
import sys
from tkinter import messagebox, Event
from tkinter.ttk import Combobox

def bytes_to_int(ba, a):
    ia = [ba[a + i] for i in range(4)]
    return ia[0] | (ia[1] << 8) | (ia[2] << 16) | (ia[3] << 24)

def zero_fill_right_shift(val, n):
    return (val % 0x100000000) >> n

def intTryParse(s):
    try:
        return int(s)
    except ValueError:
        raise ValueError("Please insert an integer value not a string")

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
    messagebox.showerror(self.appname + " Error Message", message=str(val))

def find_in_combobox(event:Event, widget:Combobox, list_of_strings: list):
    """
    Simulation for tkinter combobox search when a character key is press on keyboard

    Args:
        event (Event): key press event
        widget (Combobox): combobox to be change
        list_of_strings (list): combobox values
    """
    keypress = event.char.upper()

    if keypress in ascii_uppercase:
        for index, item in enumerate(list_of_strings):
            if item[0] == keypress:
                widget.current(index)
                widget.event_generate('<<ComboboxSelected>>')
                break
