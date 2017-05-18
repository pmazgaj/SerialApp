"""
Global settings for entire program
"""

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from SerialApp.utils.import_settings import get_section_or_param

# SERIAL_PORT_SETTINGS = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort')
# SERIAL_PORT_BYTESIZE = get_section_or_param('[SERIAL_PORT] settings.ini', 'SerialPort', 'baudrate')
# print(SERIAL_PORT_SETTINGS)
# print(SERIAL_PORT_BYTESIZE)
# MENU_SETTINGS = get_settings('[SETTINGS_MENU] menu.ini', 'MainWindow', 'iconbitmap')

matplotlib.use('TkAgg')
matplotlib.rcParams.update({'font.size': 9})  # fonts setting

PICKED_CHOICE = None
PERIOD = 2
MULTIPLIER = 2

FIGURE = plt.figure(facecolor='grey')

SHOW_X_AXIS = True  # default - X axis on
SHOW_Y_AXIS = True  #
SHOW_LEGEND = True

SHOW_GRID = True
SHOW_ALL = True

LINE_1_FLAG = True
LINE_2_FLAG = False
LINE_3_FLAG = False
LINE_4_FLAG = False
LINE_5_FLAG = False
LINE_SMA_FLAG = False
LINE_SCALED_FLAG = False
LINE_OPTIMIZED_FLAG = False
FILTER_Y_FLAG = False
FILTER_X_FLAG = False

LIST_OF_COLOURS = ['g', 'b', 'r', 'y', 'k', 'w']

FIRST_COLOR_CHOSEN = 'r'
SECOND_COLOR_CHOSEN = 'y'
THIRD_COLOR_CHOSEN = 'r'
FOURTH_COLOR_CHOSEN = 'r'
FIFTH_COLOR_CHOSEN = 'r'

BACKGROUND_STYLE = style.use('grayscale')  # default - dark_background on

BACKGROUND_COLOR = 'white'  # default background color

DRAWING_INTERVAL = 1000

# -*- coding: utf-8 -*-
LARGE_FONT = ('Verdana', 12)  # fonts setting - large
NORMAL_FONT = ('Verdana', 10)  # fonts setting - normal
SMALL_FONT = ('Verdana', 8)  # fonts setting - small

LAST_RECEIVED = ''

IS_REFRESHING = True

AUTORS_RECAP = "Przemyslaw Mazgaj\n\t\t\t\t\tPython Developer\n\t\t\t\t\tSelf employed"
