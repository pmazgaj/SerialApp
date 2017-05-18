from unittest import TestCase

from SerialApp.utils.import_settings import get_section_or_param, get_config_for_all_sections


class TestGetConfigFiles(TestCase):
    """
    Tests cases for all sections
    """
    shit = {'TkMenuChangeFrequency': {'tearoff': '1'},
            'TkMenuBar': {'command': '', 'label': 'Save log with raw data...', 'tearoff': '0', 'menu': 'menu_file'},
            'MainWindow': {'iconbitmap': "'ikona_orange.ico'", 'title': "'main window'"},
            'LineVisibleMenu': {'command2': '', 'label4': "'Line4'", 'command4': '', 'label3': "'Line3'",
                                'command5': '',
                                'command3': '', 'command1': '', 'labell': "'Line1'", 'label2': "'Line2'",
                                'label5': "'Line5'"},
            'ContainerGridColumn': {'weight': '1', 'index': '0'},
            'AuthorMenuCascade': {'label': "'O autorze'", 'menu': ''},
            'LineColorMenu': {'label3': "'Line3'", 'menu': '', 'label4': "'Line4'", 'label2': "'Line2'",
                              'labell': "'Line1'",
                              'label5': "'Line5'"}, 'TkMenuLineColor': {'label': "'Zmien kolor linii'", 'tearoff': '1'},
            'ContainerGridRow': {'weight': '1', 'index': '0'},
            'AuthorMenu': {'command': '', 'label': 'Info', 'tearoff': '0:'},
            'ContainerPack': {'expand': 'True', 'fill': 'both', 'side': 'top'},
            'MenuBar1': {'command': 'quit', 'label': 'Exit', 'tearoff': '1', 'menu': 'menu_file'},
            'TkPortMenu': {'tearoff': '1'},
            'MenuBar2': {'command': '', 'label': 'File...', 'tearoff': '1', 'menu': 'menu_file'},
            'TkMenuLineVisible': {'tearoff': '1'}}

    all_sections_valid = get_config_for_all_sections('[SETTINGS_MENU] menu.ini')
    invalid_name_of_file = get_config_for_all_sections('')
    empty_config_file = get_config_for_all_sections('dummy.ini')

    def test_get_config_for_all_sections(self):
        """Tests for getting all sections from config file"""
        self.assertIsInstance(self.all_sections_valid, dict)
        self.assertIsInstance(self.invalid_name_of_file, dict)
        self.assertEqual(self.all_sections_valid, self.shit)
        self.assertIsInstance(self.empty_config_file, dict)


class TestGetSectionOrParam(TestCase):
    serial_port_settings = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort')
    serial_port_settings_none_param = get_section_or_param('[SERIAL_PORT] settings.ini', None, 'baudrate')

    serial_port_bytesize = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort', 'baudrate')
    serial_port_wrong_param = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort', 'NaNNaN')
    # serial_port_wrong_section = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPortoryko', 'baudrate')

    serial_port_missing_param = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort')

    # serial_port_missing_section = get_section_or_param('[SERIAL_PORT] settings.ini', 'baudrate')
    # serial_port_missing_section_and_param = get_section_or_param('[SERIAL_PORT] settings.ini')

    def test_get_section_or_param(self):
        """Tests for getting only one section or param from config file"""
        self.assertIsInstance(self.serial_port_settings, dict)
        self.assertEqual(self.serial_port_settings,
                         {'bytesize': 'EIGHTBITS', 'xonxoff': '0', 'stopbits': 'STOPBITS_ONE', 'baudrate': '9600',
                          'rtscts': '0', 'port': '6', 'parity': 'PARITY_NONE', 'inter_char_timeout': 'None',
                          'timeout': '0.1'})

        self.assertIsNone(self.serial_port_settings_none_param, None)
