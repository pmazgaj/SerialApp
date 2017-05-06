"""
Module used to receive data from serial port
"""

import glob
import time
import tkinter as tk
from threading import Thread
from tkinter import StringVar, ttk

import serial
from pylab import *

from settings_files.program_settings import *

class SerialData(object):
    file_path = os.path.join(os.path.dirname(__file__), 'log.txt')
    file_exists(file_path)

    COMNUM = 7
    group = []
    baudrate1 = 115200
    data_bits = 8
    result = []
    popup =

    def __init__(self, init=50):
        try:
            self.ser = ser = serial.Serial(
                port=self.COMNUM - 1,
                baudrate=9600,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=0.1,
                xonxoff=0,
                rtscts=0,
                interCharTimeout=None
            )

            Thread(target=receiving, args=(self.ser,)).start()  # thread

            popup_msg("Port has been opened!")

        except serial.serialutil.SerialException:

            # no serial connection
            self.ser = None
            popup_msg("An error occurred ! Port was not opened !")
        else:
            pass

    def next(self):
        if not self.ser:
            return 100  # returns 100 when not connected
        # returns 100 when connected, but no data received
        for i in range(100):
            raw_line = last_received
        try:
            data = bytes.decode("utf-8")
            return float(data.strip())

        except ValueError:
            data = bytes.decode("utf-8")
            time.sleep(.001)
        return 0.

    def __del__(self):
        if self.ser:
            self.ser.close()

    def ports_available(self):
        """Check available ports on platform (for opening connection purposes)"""
        if sys.platform.startswith('win'):
            ports = ['COM' + str(i + 1) for i in range(256)]

        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this is to exclude your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')

        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')

        else:
            raise EnvironmentError('Unsupported platform')

        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.result.append(port)
            except (OSError, serial.SerialException):
                pass
        return self.result

    def set_port_spec(self):
        try:
            self.ports_available()
        except ImportError:
            # self.popup_msg("Error while importing function")
        window_set_port = tk.Tk()
        path_ico = os.path.join(os.path.dirname(__file__), 'set_ico.ico')
        window_set_port.iconbitmap(default=path_ico)
        window_set_port.wm_title("Configuration window")
        window_set_port.geometry("240x320")

        label = ttk.Label(window_set_port, text="Wybor portu: ")
        label.pack(side="top", pady=10)

        var_ = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var6 = StringVar()

        combobox = ttk.Combobox(window_set_port, textvariable=var_)
        combobox.config(values=self.result)
        combobox.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Predkosc BAUD: ")
        label.pack(side="top", pady=0)

        combobox1 = ttk.Combobox(window_set_port, textvariable=var2)
        combobox1.config(values=(50, 75, 110, 134, 150,
                                 200, 300, 600, 1200,
                                 1800, 2400, 4800, 9600, 19200,
                                 38400, 57600, 115200))
        combobox1.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Data Bits: ")
        label.pack(side="top", pady=0)

        combobox2 = ttk.Combobox(window_set_port, textvariable=var3)
        combobox2.config(values=(5, 6, 7, 8))

        combobox2.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Parity : ")
        label.pack(side="top", pady=0)

        combobox3 = ttk.Combobox(window_set_port, textvariable=var4)
        combobox3.config(values=('None', 'Odd', 'Even', 'Mark', 'Space'))
        combobox3.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Stop Bits: ")
        label.pack(side="top", pady=0)

        combobox4 = ttk.Combobox(window_set_port, textvariable=var5)
        combobox4.config(values=(1, 1.5, 2))
        combobox4.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Flow control: ")
        label.pack(side="top", pady=0)

        combobox5 = ttk.Combobox(window_set_port, textvariable=var6)
        combobox5.config(values=('XON', 'X_OFF'))
        combobox5.pack(side="top", pady=0)

        def change_port_data():

            b_r = combobox1.get()
            c_n = combobox.get()
            d_b = combobox2.get()
            p_ = combobox3.get()
            s_b = combobox4.get()
            f_c = combobox5.get()

            self.baudrate1 = ''.join(x for x in b_r if x.isdigit())
            self.COMNUM = ''.join(x for x in c_n if x.isdigit())
            self.data_bits = ''.join(x for x in d_b if x.isdigit())
            self.parity = ''.join(x for x in p_)
            self.stop_bits = ''.join(x for x in s_b if x.isdigit())
            self.flow_control = ''.join(x for x in f_c)

            self.group.append(self.baudrate1)
            self.group.append(self.COMNUM)
            self.group.append(self.data_bits)
            self.group.append(self.parity)
            self.group.append(self.stop_bits)
            self.group.append(self.flow_control)

            print("Ustawiono : {}".format(self.group))

            print("Otworzono port {}".format(c_n))

            window_set_port.destroy()

        button1 = ttk.Button(window_set_port, text="Ustaw",
                             command=lambda: change_port_data())  # podajemy parametr i zapętlamy
        button1.pack()




def start_stop(works_t_f):
    if works_t_f == 'startuj':
        popup_msg('Odświeżanie danych zostało wznowione')

    elif works_t_f == 'stopuj':
        popup_msg('Odświeżanie danych zostało wstrzymane')


def receiving(ser):
    global last_received
    global bytes
    global data
    global data_count
    data_count = 0
    while True:

        bytes = ser.readline()  # Read from Serial Port
        data = bytes.decode("utf-8")  # dlugosc linii do odczytu danych = 36
        if len(data) > 35:
            timer()
            data_count += 1
            open_file()
        else:
            pass

