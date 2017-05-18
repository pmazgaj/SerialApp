"""
Module to import program settings from ini file
"""
import configparser
import os
from SerialApp.settings_files.program_paths import FOLDER_SETTINGS_INI

__author__ = "Przemek"


def get_config_for_all_sections(file_path: str) -> dict:
    """
    Open .*.ini files, and get global config for all sections
    :param file_path: exact path for file
    :return:
    """
    all_sections = dict()

    full_path = os.path.join(FOLDER_SETTINGS_INI, file_path)
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read(full_path)

    for section in config.sections():
        all_sections[section] = dict(config.items(section))
    return all_sections


def get_section_or_param(file_path: str, section: str = None, param: str = None) -> dict:
    """
    Open .*.ini files, and get config for one and only section
    :param file_path: exact path for file
    :param section: Section to be taken from ini file
    :param param: Optional arg for param (default=None)
    :return:
    """
    if section is None:
        return None
    full_path = os.path.join(FOLDER_SETTINGS_INI, file_path)
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read(full_path)

    section = dict(config.items(section))

    return section if param is None else section.get(param, None)
