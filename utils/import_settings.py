"""
Module to import program settings from ini file
"""
import configparser
from settings_files.program_paths import *

__author__ = "Przemek"


def get_config_for_all_sections(file_path):
    all_sections = dict()

    full_path = FOLDER_SETTINGS_INI + "\\" + file_path
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read(full_path)

    for section in config.sections():
        all_sections[section] = dict(config.items(section))
    return all_sections


def get_config_for_one_section(file_path, section):
    """Open .*.ini files, and get exact section for these"""
    full_path = FOLDER_SETTINGS_INI + "\\" + file_path
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read(full_path)

    return dict(config.items(section))


def get_config_for_one_param(file_path, section, param):
    """Open .*.ini files, and get sections for those"""
    full_path = FOLDER_SETTINGS_INI + "\\" + file_path
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read(full_path)
    config.sections()

    return config.get(section, param)

    # print(settings.sections())
    # return settings.items()
    # return settings.get(section, param)
