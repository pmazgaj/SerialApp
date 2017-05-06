"""
Module to parse .*csv files into list of values.
Possible - line by line (yield) and all_data.
"""
import csv
from settings_files.program_settings import *

__author__ = "Przemek"


class FileHandler:
    @staticmethod
    def get_data_line_by_line(file) -> list:
        """Parse data to list, from given file, step by step"""
        with open(FOLDER_CSV_FILES + '\\' + file) as file:
            reader = csv.reader(file)
            print(reader)
            for row in reader:
                yield row

    @staticmethod
    def get_all_data_from_file(file) -> list:
        """Return list of all lines in file (as list)"""
        lines = []
        with open(FOLDER_CSV_FILES + '\\' + file) as file:
            reader = csv.reader(file)
            for row in reader:
                lines.append(row)
        return lines

# csv_handler = FileHandler()

# a = csv_handler.get_data_line_by_line('test.csv')
# b = csv_handler.get_all_data_from_file('test.csv')


