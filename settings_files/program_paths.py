"""
Module to store program paths
"""
import os

__author__ = "Przemek"

# paths used in project
FOLDER_PROJECT_PATH = os.path.abspath('..')
FOLDER_ASSETS_ICONS = os.path.join(FOLDER_PROJECT_PATH, 'assets', 'icons')
FOLDER_SETTINGS_INI = os.path.join(FOLDER_PROJECT_PATH, 'settings_files', 'ini')

FOLDER_CSV_FILES = os.path.join(FOLDER_PROJECT_PATH, 'csv_files')

print(FOLDER_ASSETS_ICONS)
print(FOLDER_PROJECT_PATH)
print(FOLDER_SETTINGS_INI)
print(FOLDER_CSV_FILES)
