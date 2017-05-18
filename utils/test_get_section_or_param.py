from unittest import TestCase

from SerialApp.utils.import_settings import get_section_or_param


class TestGetConfigFiles(TestCase):
    serial_port_settings = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort')
    serial_port_settings_none_param = get_section_or_param('[SERIAL_PORT] settings.ini', None, 'baudrate')

    serial_port_bytesize = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort', 'baudrate')
    print(serial_port_settings)
    serial_port_wrong_param = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort', 'NaNNaN')
    # serial_port_wrong_section = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPortoryko', 'baudrate')

    serial_port_missing_param = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort')

    # serial_port_missing_section = get_section_or_param('[SERIAL_PORT] settings.ini', 'baudrate')
    # serial_port_missing_section_and_param = get_section_or_param('[SERIAL_PORT] settings.ini')

    def test_get_section_or_param(self):
        self.assertIsInstance(self.serial_port_settings, dict)
        self.assertEqual(self.serial_port_settings, {'bytesize': 'EIGHTBITS', 'xonxoff': '0', 'stopbits': 'STOPBITS_ONE', 'baudrate': '9600', 'rtscts': '0', 'port': '6', 'parity': 'PARITY_NONE', 'inter_char_timeout': 'None', 'timeout': '0.1'})

        self.assertIsNone(self.serial_port_settings_none_param, None)

        print(self.serial_port_settings)
        # print(serial_port_bytesize)

    def test_get_config_for_all_sections(self):
        pass
