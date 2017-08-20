"""
Module to store program paths
"""
import os

__author__ = "Przemek"

# paths used in project
FOLDER_PROJECT_PATH = os.path.dirname(__file__)
FOLDER_ASSETS_ICONS = os.path.join(FOLDER_PROJECT_PATH, 'assets', 'icons')
FOLDER_CONF_YML = os.path.join(FOLDER_PROJECT_PATH, 'conf')

FOLDER_CSV_FILES = os.path.join(FOLDER_PROJECT_PATH, 'csv_files')

# print(FOLDER_CONF_YML)
# print(FOLDER_PROJECT_PATH)
# print(FOLDER_ASSETS_ICONS)
# print(FOLDER_SETTINGS_INI)
# print(FOLDER_CSV_FILES)
