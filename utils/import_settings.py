"""
Module to import program settings from ini file
"""
import configparser
from settings_files.program_paths import *

__author__ = "Przemek"


def get_settings(file_path, section, param):
    """Open .*.ini files, and get sections for those"""
    full_path = FOLDER_SETTINGS_INI + "\\" + file_path
    print(full_path)
    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read(full_path)

    settings.sections()

    return settings.get(section, param)
