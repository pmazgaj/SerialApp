"""
Module handling popups
"""
import tkinter.messagebox
from abc import ABC, abstractmethod

__author__ = "Przemek"


class Popup(ABC):
    """
    Base class for popups
    """

    @abstractmethod
    def __init__(self):
        ...


class PopupInfo(Popup):
    def __init__(self, message_title='Info', message_info=''):
        super(PopupInfo, self).__init__()
        tkinter.messagebox.showinfo(message_title, message_info)


class PopupWarning(Popup):
    def __init__(self, message_title='Warning', message_info=''):
        super(Popup, self).__init__()
        tkinter.messagebox.showwarning(message_title, message_info)


class PopupError(Popup):
    def __init__(self, message_title='Error', message_info=''):
        super(Popup, self).__init__()
        tkinter.messagebox.showwarning(message_title, message_info)

# Popup()
# PopupInfo('Lin Thizzy', 'Lin Thizzy')
# PopupWarning('Lin Thizzy', 'Lin Thizzy')
# PopupError('Znów pioruny', 'Oraz deszcze na żoli')
