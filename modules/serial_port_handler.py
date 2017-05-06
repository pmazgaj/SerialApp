"""
Module used to receive data from serial port
"""

import glob
import time
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
    interCharTimeout = SERIAL_PORT_SETTINGS['inter_char_timeout']
    port = ''
    # def __init__(self):
    #     try:
    #         self.ser = ser = serial.Serial(port=self.com_number - 1,
    #                                        baudrate=self.baudrate,
    #                                        bytesize=serial.EIGHTBITS,
    #                                        parity=serial.PARITY_NONE,
    #                                        stopbits=serial.STOPBITS_ONE,
    #                                        timeout=0.1,
    #                                        xonxoff=0,
    #                                        rtscts=0,
    #                                        interCharTimeout=None
    #                                        )
    #
    #     except serial.serialutil.SerialException:
    #
    #         # no serial connection
    #         self.ser = None
    #     else:
    #         pass
    ser = None

    def __del__(self):
        """Close serial port connection (if opened)"""
        if self.ser:
            self.ser.close()

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

    @staticmethod
    def ports_available():
        """Check available ports on platform (for opening connection purposes)"""
        result = []
        if sys.platform.startswith('win'):
            print('Your platform is windows')
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

    @staticmethod
    def start(is_stopped):
        """If visualising stopped refresh, else do None"""
        if is_stopped:
            return True
        else:
            return False

    @staticmethod
    def stop(is_stopped):
        if not is_stopped:
            return True
        else:
            return False

    @staticmethod
    def receiving(ser):
        data_count = 0
        while True:

            line_to_decode = ser.readline()  # Read from Serial Port
            data = line_to_decode.decode("utf-8")  # dlugosc linii do odczytu danych = 36
            if len(data) > 35:
                data_count += 1
            else:
                pass

    def __str__(self):
        return "Created serial port: {} on {}\nBaudrate: {}\nBytesize: {}\nStopbits: {}"\
            .format(self.port, self.port, self.port, self.port, self.port)

serial_port_test = SerialData()
a = serial_port_test.ports_available()

print(a)
