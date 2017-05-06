"""
Module used to receive data from serial port
"""

import glob
import threading
import time
import tkinter as tk
from functools import reduce
from threading import Thread
from tkinter import StringVar, ttk

import serial
from pylab import *

from settings_files.program_settings import *


def start_stop(works_t_f):
    if works_t_f == 'startuj':
        popup_msg('Odświeżanie danych zostało wznowione')

    elif works_t_f == 'stopuj':
        popup_msg('Odświeżanie danych zostało wstrzymane')


class Filter(threading.Thread):
    def __init__(self, data, out):
        threading.Thread.__init__(self)
        self.data = data
        self.out = out
        self.jump = 1
        self.multiplier = 2
        self.period = 2  # splitter...
        self.weights = 0
        self.new_data_set = []
        self.a = []
        self.val1 = []
        self.val2 = []
        self.val3 = []
        self.val4 = []
        self.val5 = []
        self.val6 = []
        self.logfile = open('log.txt', 'a')

    def run(self):
        file = open(self.out, "a")

        file.write(str(self.data_scale(self.multiplier)))

        file.close()
        time.sleep(0.005)

    def data_scale(self, multiplier):
        self.multiplier = multiplier  # setting up MULTIPLIER
        a = [[], [], [], [], [], [], []]
        g = [[], [], [], [], [], [], []]  # Lista na siedem list danych z arduino
        for i, value in enumerate(self.data.split(" ")):
            a[i].append(float(value) * self.multiplier)
        return str(a).replace('[', '').replace(']', '').replace(',', '') + "\n"

    def unique_values(self):  #
        seen = set()  # set...
        for i, value in enumerate(self.data.split(' ')):
            self.a.append(value)
            values_list = []
            if (len(self.a)) >= 7:
                q, w, e, r, t, y, m = self.a
                values_list.extend((q, w, e, r, t, y))

                print(set(values_list))
            if value not in seen:
                yield value
                seen.add(value)

    def raw_data(self):
        self.logfile.write(str(data))
        self.logfile.close()


def timer():
    calc_time = time.clock()
    return int(calc_time)


def calculate_freq():
    if timer() > 0:
        sample_time.append(timer() / data_count)

        def average_value(values):
            simple_average = sum(values) / len(values)
            return simple_average

        avg_t = average_value(sample_time)
        freq.append(1 / avg_t)

        if avg_t <= sample_time[-1]:
            pass

        else:
            print("maly")

        avg_freq = average_value(freq)
        nyquist_freq = (0.5 * freq[-1])

        popup_msg("Czas całkowity: {} s\n"
                  "Czas obecnej próbki: {:.3} s\n"
                  "Średni czas próbkowania: {:.3} s\n"
                  "Częstotliwość: {:.3} Hz\n"
                  "Średnia częstotliwość: {:.3} Hz\n"
                  "Nyquist : {:.3} Hz".format(timer(), sample_time[-1], avg_t, freq[-1], avg_freq, nyquist_freq))


def main():
    t1 = Filter(data, 'log_raw.txt')
    t2 = Filter(data, 'log_skaluj.txt')
    t3 = Filter(data, 'log_srednia_kroczaca.txt')
    t4 = Filter(data, 'log_unique.txt')
    t5 = Filter(data, 'log_t5.txt')
    t.append(t1)
    t.append(t2)
    t.append(t3)
    t.append(t4)
    t.append(t5)

    if IS_REFRESHING is False:
        for each_thread in t:
            each_thread.stop()

    elif IS_REFRESHING is True:
        t1.raw_data()

    else:
        popup_msg("CONDOMINIUM GERMAN-RUSSIAN UNDER ESTIMATE OF JEWISH LEAD")


def open_file():
    try:
        main()

    except Exception as exception2:
        return exception2


def file_exists(path_given):  # usuniecie pliku, na poczatku działania
    if os.path.isfile(path_given):
        os.unlink(path_given)
    else:
        pass


def change_granularity(x, y, divider):
    gran_x = x
    gran_y = y

    changed_gran_x = []
    changed_gran_y = []

    g_x = len(x)
    while g_x > divider:
        x_list = gran_x[g_x - divider:g_x]
        x_avg = reduce(lambda x, y: x + y, x_list) / float(len(x_list))

        y_list = gran_y[g_x - divider:g_x]
        y_avg = reduce(lambda x, y: x + y, y_list) / float(len(y_list))

        changed_gran_x.append(x_avg)
        changed_gran_y.append(y_avg)

        g_x -= divider

        # print(changed_gran_x)
        # print(changed_gran_y)
        return changed_gran_x, changed_gran_y


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


class SerialData(object):
    file_path = os.path.join(os.path.dirname(__file__), 'log.txt')
    file_exists(file_path)

    COMNUM = 7
    group = []
    baudrate1 = 115200
    data_bits = 8
    result = []

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
            self.ports_avalaible()
        except ImportError:
            self.popup_msg("Error while importing function")
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

            print("Ustawiono :", self.group)

            print("Otworzono port ", c_n)

            window_set_port.destroy()

        button1 = ttk.Button(window_set_port, text="Ustaw", command=lambda: change_port_data())  # podajemy parametr i zapętlamy
        button1.pack()
