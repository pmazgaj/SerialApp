"""
Define all pages for the Serial Port Handling.
"""
import tkinter as tk
from tkinter import ttk

from SerialApp.conf.program_settings import LARGE_FONT
from .pages import StartPage


class PageChangeSerialPort(tk.Frame):
    """Window with settings for changing serial port"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Serial Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # lambda - to use parameter in function
        button = ttk.Button(self, text="Back to start page",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()


class PageConfigSerialPort(tk.Frame):
    # label_icon = os.path.join(FOLDER_ASSETS_ICONS, 'set_ico.ico')

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Serial Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # lambda - to use parameter in function
        button = ttk.Button(self, text="Back to start page",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()
        # raise NotImplementedError('not yet implemented')
