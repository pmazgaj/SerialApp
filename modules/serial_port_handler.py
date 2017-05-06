"""
Module used to receive data from serial port
"""

import glob
import time
import tkinter as tk
from tkinter import StringVar, ttk
import serial
from pylab import *
from settings_files.program_settings import SERIAL_PORT_SETTINGS


class SerialData:
    com_number = SERIAL_PORT_SETTINGS['port']
    baudrate = SERIAL_PORT_SETTINGS['baudrate']
    bytesize = SERIAL_PORT_SETTINGS['bytesize']
    parity = SERIAL_PORT_SETTINGS['parity']
    stopbits = SERIAL_PORT_SETTINGS['stopbits']
    timeout = SERIAL_PORT_SETTINGS['timeout']
    xonxoff = SERIAL_PORT_SETTINGS['xonxoff']
    rtscts = SERIAL_PORT_SETTINGS['rtscts']
    interCharTimeout = SERIAL_PORT_SETTINGS['interCharTimeout']

    def __init__(self):
        try:
            self.ser = ser = serial.Serial(port=self.com_number - 1,
                                           baudrate=self.baudrate,
                                           bytesize=serial.EIGHTBITS,
                                           parity=serial.PARITY_NONE,
                                           stopbits=serial.STOPBITS_ONE,
                                           timeout=0.1,
                                           xonxoff=0,
                                           rtscts=0,
                                           interCharTimeout=None
                                           )

        except serial.serialutil.SerialException:

            # no serial connection
            self.ser = None
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
        """Close serial port connection (if opened)"""
        if self.ser:
            self.ser.close()

    @staticmethod
    def ports_available():
        """Check available ports on platform (for opening connection purposes)"""
        result = []
        if sys.platform.startswith('win'):
            ports = ['COM{}'.format(i + 1) for i in range(0, 256)]

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
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result


    def start_stop(self, is_stopped):
        """If visualising stopped refresh, else do None"""
        if is_stopped:
            return True
        else:
            return False

    def stop(self, is_stopped):
        if

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
