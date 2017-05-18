"""
Main module - handle everything from outside classes
"""
import tkinter as tk
from SerialApp.modules.GUI.pages import StartPage, PageOne, PageTwo


class MainApplication(tk.Tk):
    """Main application handler (controller for GUI)"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(index=0, weight=1)
        container.grid_columnconfigure(index=0, weight=1)

        self.frames = {}
        self.add_frames(container)
        self.show_frame(StartPage)

    def add_frames(self, container: tk.Frame):
        """
        Specifies which frames are added into application
        :param container:
        :return:
        """
        for f_frame in (StartPage, PageOne, PageTwo):
            frame = f_frame(container, self)
            self.frames[f_frame] = frame
            frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(self, controller: type):
        """
        Show single frame from the dictionary
        :param controller:
        :return:
        """
        frame = self.frames[controller]

        # set frame (page) to the front
        frame.tkraise()


# create main application and then run main loop
APP = MainApplication()
APP.mainloop()
