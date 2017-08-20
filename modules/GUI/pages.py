"""
Define all pages for the application.
"""
import tkinter as tk
from tkinter import ttk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from SerialApp.conf.program_settings import LARGE_FONT

matplotlib.use("TkAgg")


class StartPage(tk.Frame):
    """Start page class"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # lambda - to use parameter in function
        button = ttk.Button(self, text="Visit page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit graph page",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):
    """Page one class"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page one', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # lambda - to use parameter in function
        button = ttk.Button(self, text="Back to start page",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        button2 = ttk.Button(self, text="Go to page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    """Page two class"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page Two', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # lambda - to use parameter in function
        button = ttk.Button(self, text="Start Page",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        figure = Figure(figsize=(5, 5), dpi=100)
        subplot = figure.add_subplot(111)
        subplot.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 7, 8, 9, 10, 11, 4])
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.show()

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()

        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
