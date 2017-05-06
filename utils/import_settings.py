"""
Module to import settings from ini file
"""
import configparser
from settings_files.program_settings import *

__author__ = "Przemek"


def get_settings(settings_file, section, param):
    full_path = FOLDER_SETTINGS_INI + "\\" + settings_file

    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read(full_path)

    # print(a)
    settings.sections()

    return settings.get(section, param)


a = get_settings('[SETTINGS_MENU] menu.ini', 'MainWindow', 'iconbitmap')
print(a)
