"""
Get config for yml files (section, or a single param)
"""
import os
import yaml

from SerialApp.program_paths import FOLDER_CONF_YML

__author__ = "Przemek"


def get_all_sections(file_name: str) -> dict:
    """
    Open .*.yml files, and get global config for all sections
    :param file_name: exact path for file
    :return:
    """
    file_path = os.path.join(FOLDER_CONF_YML, file_name)
    with open(file_path) as yml_file:
        config = yaml.load(yml_file)

    return config


def get_section_or_param(file_name: str, section: str = None, param: str = None) -> dict:
    """
    Open .*.yml files, and get config for one and only section
    :param file_name: exact path for file
    :param section: Section to be taken from ini file
    :param param: Optional arg for param (default=None)
    :return:
    """
    file_path = os.path.join(FOLDER_CONF_YML, file_name)
    if section is None:
        return None

    with open(file_path) as yml_file:
        config = yaml.load(yml_file)
        config = config.get(section, None)

        if param is not None:
            config = config.get(param, None)
    return config


# get timeout for section SerialPort
timeout = get_section_or_param('settings_serial_port.yaml', 'SerialPort', 'timeout')

# get Section serial port
section_serial = get_section_or_param('settings_serial_port.yaml', 'SerialPort')

# get wrong section from multiple sections file
wrong_section_from_multiple = get_section_or_param('settings_menu.yaml', 'SerialPort')
# print(wrong_section_from_multiple)

# get wrong section from multiple sections file
section_line_color_from_multiple = get_section_or_param('settings_menu.yaml', 'LineColorMenu')
# print(section_line_color_from_multiple)

# get_all_sections
all_sections = get_all_sections('settings_menu.yaml')
