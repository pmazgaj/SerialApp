#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- Encoding: utf-8 -*-
import json
import urllib.request

import matplotlib.animation as animation_plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from modules import serial_port_handler as ser_mod
from modules.GUI.menu import *
from settings_files.program_settings import *


class Main:
    # settings_files = Settings()
    pass


# the_class = ser_mod.SerialData()


def save_raw_file():  # imported Tkinter as tk, filedialog used
    tk.filedialog.asksaveasfile(mode='w', defaultextension=".csv", title="Export file...")  # open file...

    file_path = os.path.join(os.path.dirname(__file__), 'log.txt')
    ser_mod.file_exists(file_path)


def set_interval(interval_set):
    global interval
    if interval_set == "1ms" or interval_set == 1:
        interval = 1
        return interval

    elif interval_set == "150ms" or interval_set == 150:
        interval = 150

        return interval
    elif interval_set == "100ms" or interval_set == 100:
        interval = 100

        return interval
    elif interval_set == "200ms" or interval_set == 200:
        interval = 200

        return interval
    elif interval_set == "500ms" or interval_set == 500:
        interval = 500

        return interval
    elif interval_set == "600ms" or interval_set == 600:
        interval = 600

        return interval
    elif interval_set == "1000ms" or interval_set == 1000:
        interval = 1000
        #        ani2._interval = DRAWING_INTERVAL
        return interval
    elif interval_set == "3000ms" or interval_set == 3000:
        interval = 3000

        print(interval)
        return interval
    elif interval_set == "5000ms" or interval_set == 5000:
        interval = 5000

        print(interval)
        return interval


def set_lines_color(color):
    global color_tab
    global chosen_color_1
    global chosen_color_2
    global chosen_color_3
    global chosen_color_4
    global chosen_color_5

    if (line_1 is True) and (color == 'blue'):
        chosen_color_1 = color_tab[1]

    elif (line_1 is True) and (color == 'white'):
        chosen_color_1 = color_tab[5]

    elif (line_1 is True) and (color == 'yellow'):
        chosen_color_1 = color_tab[3]

    elif (line_1 is True) and (color == 'red'):
        chosen_color_1 = color_tab[2]

    elif (line_1 is True) and (color == 'green'):
        chosen_color_1 = color_tab[0]

    elif (line_1 is True) and (color == 'black'):
        chosen_color_1 = color_tab[4]

    #################################################

    elif (line_2 is True) and (color == 'blue'):
        chosen_color_2 = color_tab[1]

    elif (line_2 is True) and (color == 'white'):
        chosen_color_2 = color_tab[5]

    elif (line_2 is True) and (color == 'yellow'):
        chosen_color_2 = color_tab[3]

    elif (line_2 is True) and (color == 'red'):
        chosen_color_2 = color_tab[2]

    elif (line_2 is True) and (color == 'green'):
        chosen_color_2 = color_tab[0]

    elif (line_2 is True) and (color == 'black'):
        chosen_color_1 = color_tab[4]

    #################################################

    elif (line_3 is True) and (color == 'blue'):
        chosen_color_3 = color_tab[1]

    elif (line_3 is True) and (color == 'white'):
        chosen_color_3 = color_tab[5]

    elif (line_3 is True) and (color == 'yellow'):
        chosen_color_3 = color_tab[3]

    elif (line_3 is True) and (color == 'red'):
        chosen_color_3 = color_tab[2]

    elif (line_3 is True) and (color == 'green'):
        chosen_color_3 = color_tab[0]

    elif (line_3 is True) and (color == 'black'):
        chosen_color_1 = color_tab[4]
        ################################################
    #################################################

    elif (line_4 is True) and (color == 'blue'):
        chosen_color_4 = color_tab[1]

    elif (line_4 is True) and (color == 'white'):

        chosen_color_4 = color_tab[5]

    elif (line_4 is True) and (color == 'yellow'):
        chosen_color_4 = color_tab[3]

    elif (line_4 is True) and (color == 'red'):
        chosen_color_4 = color_tab[2]

    elif (line_4 is True) and (color == 'green'):
        chosen_color_4 = color_tab[0]

    elif (line_4 is True) and (color == 'black'):
        chosen_color_1 = color_tab[4]
        ################################################

    elif (line_5 is True) and (color == 'blue'):
        chosen_color_5 = color_tab[1]

    elif (line_5 is True) and (color == 'white'):
        chosen_color_5 = color_tab[5]

    elif (line_5 is True) and (color == 'yellow'):
        chosen_color_5 = color_tab[3]

    elif (line_5 is True) and (color == 'red'):
        chosen_color_5 = color_tab[2]

    elif (line_5 is True) and (color == 'green'):
        chosen_color_5 = color_tab[0]

    elif (line_5 is True) and (color == 'black'):
        chosen_color_1 = color_tab[4]


def set_period(what_to_use):  # filtering axis y
    filter_range = tk.Tk()
    if what_to_use in ("SMA", "Multiplier"):
        filter_range.wm_title('Set {}'.format(what_to_use))
        label = ttk.Label(filter_range, text=what_to_use)
        label.pack(side='top', fill='x', pady=10)

    e = ttk.Entry(filter_range)

    e.insert(0, 2)
    e.pack()
    e.focus_set()

    if what_to_use == "SMA":
        def callback():

            global period
            period = []
            period.insert(0, int(e.get()))
            filter_range.destroy()
            ser_mod.popup_msg('SMA PERIOD set manually!')

    elif what_to_use == "Multiplier":
        def callback():
            global multiplier
            multiplier = []
            multiplier.insert(0, float(e.get()))
            filter_range.destroy()
            ser_mod.popup_msg('Multiplier set manually!')

    b = ttk.Button(filter_range, text='Set', width=10, command=callback)

    b.pack()
    tk.mainloop()


def set_filter():  # filtering axis y
    global filter_y, filter_x
    y_min = []
    y_max = []

    if filter_y is False:
        filter_y = True
    else:
        filter_y = False

    if filter_x is False:
        filter_x = True
    else:
        filter_x = False

    filter_range = tk.Tk()
    filter_range.wm_title('Ustaw zakres filtru')
    label = ttk.Label(filter_range, text='Y min')
    label.pack(side='top', fill='x', pady=10)

    e = ttk.Entry(filter_range)
    e1 = ttk.Entry(filter_range)

    e.insert(0, 500)
    e1.insert(0, 830)

    e.pack()
    e.focus_set()

    label = ttk.Label(filter_range, text='Y max')
    label.pack(side='top', fill='x', pady=10)

    e1.pack()
    e1.focus_set()

    def callback():

        global y_min, y_max
        group = []
        periods = (float(e.get()), float(e1.get()))

        group.append('Y min, Y max')
        group.append(periods)

        y_min.insert(0, int(e.get()))
        y_max.insert(0, int(e1.get()))

        filter_range.destroy()
        ser_mod.popup_msg('Przedział Y ustalony manualnie!')

    b = ttk.Button(filter_range, text='Ustaw', width=10, command=callback)

    b.pack()
    tk.mainloop()


def show_elements(element):
    global show_X_axis, show_Y_axis, show_grid, show_legend, show_all

    if element == 'X_axis':
        show_X_axis = False if show_X_axis else True

    elif element == 'Y_axis':
        show_Y_axis = False if show_Y_axis else True

    elif element == 'Grid':
        show_grid = False if show_grid else True

    elif element == 'Legenda':
        show_legend = False if show_legend else True

    elif element == 'Wszystko' and (show_legend == show_grid == show_X_axis == show_Y_axis):
        if show_legend == show_grid == show_X_axis == show_Y_axis:
            if show_legend is True:
                show_legend = show_grid = show_X_axis = show_Y_axis = False
            else:
                show_legend = show_grid = show_X_axis = show_Y_axis = True
        else:
            pass


def print_lines(line_number):
    global line_1
    global line_2
    global line_3
    global line_4
    global line_5
    global line_sma
    global line_scaled
    global line_optimized

    if line_number == 'line1':
        line_1 = False if line_1 else True

    if line_number == 'line2':
        line_2 = False if line_2 else True

    if line_number == 'line3':
        line_3 = False if line_3 else True

    if line_number == 'line4':
        line_4 = False if line_4 else True

    if line_number == 'line5':
        line_5 = False if line_5 else True

    if line_number == 'linia_sma':
        line_sma = False if line_sma else True

    if line_number == 'LINE_SCALED_FLAG':
        line_scaled = False if line_scaled else True

    if line_number == 'LINE_OPTIMIZED_FLAG':
        line_optimized = False if line_optimized else True


def bg_set(tlo):
    global bg_style
    global bg_color

    if tlo == 'white':
        bg_color = ''
        bg_color = 'white'

    elif tlo == 'blue':
        bg_color = ''
        bg_color = 'blue'

    elif tlo == 'yellow':
        bg_color = ''
        bg_color = 'yellow'

    elif tlo == 'grey':
        bg_color = ''
        bg_color = 'grey'

    elif tlo == 'ggplot':
        bg_style = ''
        bg_style = style.use('ggplot')

    elif tlo == 'bmh':
        bg_style = ''
        bg_style = style.use('bmh')

    elif tlo == 'dark_background':
        bg_style = ''
        bg_style = style.use('dark_background')
        ser_mod.popup_msg('Styl domyślny')

    elif tlo == 'grayscale':
        bg_style = ''
        bg_style = style.use('grayscale')

    elif tlo == 'fivethirtyeight':
        bg_style = ''
        bg_style = style.use('fivethirtyeight')


class Main(tk.Tk):
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    BuildMenu()
    show_frame(HomePage)  # main page


def choose_data_source(argument):
    global picked_choice

    if argument in ('arduino', 'random'):
        picked_choice = argument

    elif argument == 'random':
        picked_choice = ''
        picked_choice = 'random'


def moving_average(values, window):
    weights = np.repeat(values, window) / window
    simple_average = np.convolve(values, weights, 'valid')[:len(values)]
    return simple_average


def scale_lines(values, chosen_multiplier):
    return values * chosen_multiplier


def graph_data(i):
    if ser_mod.IS_REFRESHING:  # default true
        if picked_choice == 'arduino':
            try:
                f.clf()  # cleaning fig
                try:
                    a = plt.subplot2grid((5, 4), (0, 0), rowspan=4, colspan=4, axisbg='#07000d')
                    a_2 = plt.subplot2grid((5, 4), (4, 0), sharex=a, rowspan=1, colspan=4, axisbg='#07000d')

                    temp_c, temp_k, temp_f, resistance, stan, voltage_1, voltage_2 = np.loadtxt('log.txt',
                                                                                                unpack=True,
                                                                                                delimiter=' ')
                    x = np.arange(len(temp_c))

                    if len(temp_c) > 10:  # not working yet...
                        list(temp_c).pop(0)

                    if filter_y is True:  # filtering y_data for both charts, cause they are connected
                        a.set_ylim([y_min[0], y_max[0]])  # filtering data!
                        a_2.set_ylim([y_min[0], y_max[0]])  # filtering data!

                    f.suptitle('Arduino Data', fontsize=20)

                    a.grid(b=show_grid, color='w')
                    a.yaxis.label.set_color('w')
                    a.spines['bottom'].set_color('#5998ff')
                    a.spines['top'].set_color('#5998ff')
                    a.spines['left'].set_color('#5998ff')
                    a.spines['right'].set_color('#5998ff')
                    a.tick_params(axis='y', colors='w')
                    a.xaxis.set_major_locator(mticker.MaxNLocator(10))

                    rez_min = resistance.min()
                    temp_c_min = temp_c.min()
                    temp_k_min = temp_k.min()
                    temp_f_min = temp_f.min()
                    stan_min = stan.min()

                    plt.setp(a.get_xticklabels(), visible=False)
                    plt.setp(a_2.get_xticklabels(), visible=show_X_axis)
                    plt.setp(a.get_yticklabels(), visible=show_Y_axis)

                    plt.subplots_adjust(left=.09, bottom=.14, right=.94, top=.95, wspace=.20, hspace=.0)
                    plt.suptitle('', color='w')

                    a_2.axes.yaxis.set_ticklabels([])  # tick labels off on second graph
                    a_2.spines['bottom'].set_color('#5998ff')
                    a_2.spines['top'].set_color('#5998ff')
                    a_2.spines['left'].set_color('#5998ff')
                    a_2.spines['right'].set_color('#5998ff')

                    a.grid(visible=show_grid)

                    a_2.tick_params(axis='x', colors='w')
                    a_2.tick_params(axis='y', colors='w')

                    if bg_color == 'blue':
                        rect = a.patch
                        rect1 = a_2.patch
                        rect.set_facecolor('blue')
                        rect1.set_facecolor('blue')
                        a.grid(b=show_grid, color='g')

                    elif bg_color == 'white':
                        rect = a.patch
                        rect1 = a_2.patch
                        rect.set_facecolor('white')
                        rect1.set_facecolor('white')
                        a.grid(b=show_grid, color='g')

                    elif bg_color == 'yellow':
                        rect = a.patch
                        rect1 = a_2.patch
                        rect.set_facecolor('yellow')
                        rect1.set_facecolor('yellow')
                        a.grid(b=show_grid, color='r')

                    elif bg_color == 'grey':
                        rect = a.patch
                        rect1 = a_2.patch
                        rect.set_facecolor('grey')
                        rect1.set_facecolor('grey')
                        a.grid(b=show_grid, color='black')

                    if line_1:

                        a.plot(x, resistance, chosen_color_1, label='Resistance')

                        a_2.fill_between(x, rez_min, resistance, facecolor='#00ffe8', alpha=.5)
                        if show_legend:
                            a.legend()

                        if line_sma:
                            ap2 = moving_average(resistance, period)
                            a.plot(x[len(x) - len(ap2):], ap2, 'y--', label='SMA')
                            a_2.plot(ap2, 'y--')
                            if show_legend:
                                a.legend()

                        if line_scaled:
                            multiply_value = scale_lines(resistance, multiplier)
                            a.plot(x, multiply_value, 'y--', label='Scalled line')
                            # a.plot(ar, er, 'ro', label='Scalled line')
                            a_2.plot(multiply_value, 'y--')
                            if show_legend:
                                a.legend()

                    if line_optimized and not line_1:
                        axs, bxs = (ser_mod.change_granularity(x, resistance, 50))
                        print(axs)
                        print(x)
                        print(bxs)
                        a.plot(x, bxs)

                    if line_2:

                        a.plot(x, temp_c, chosen_color_2, label='Celsius')

                        a_2.fill_between(x, temp_c_min, temp_c, facecolor='#00ffe8', alpha=.5)
                        if show_legend:
                            a.legend()

                        if line_sma:
                            ap2 = moving_average(temp_c, period)
                            a.plot(x[len(x) - len(ap2):], ap2, 'y--', label='SMA')
                            a_2.plot(ap2, 'y--')
                            if show_legend:
                                a.legend()

                        if line_scaled:
                            multiply_value = scale_lines(temp_c, multiplier)
                            a.plot(x, multiply_value, 'co', label='Scalled line')
                            a_2.plot(multiply_value, 'co')
                            if show_legend:
                                a.legend()

                    if line_3:

                        a.plot(x, temp_k, chosen_color_3, label='Kelvin')

                        a_2.fill_between(x, temp_k_min, temp_k, facecolor='#00ffe8', alpha=.5)
                        if show_legend:
                            a.legend()

                        if line_sma:
                            ap2 = moving_average(temp_k, period)
                            a.plot(x[len(x) - len(ap2):], ap2, 'y--', label='SMA')
                            a_2.plot(ap2, 'y--')
                            if show_legend:
                                a.legend()

                        if line_scaled:
                            multiply_value = scale_lines(temp_k, multiplier)
                            a.plot(x, multiply_value, 'wo', label='Scalled line')
                            a_2.plot(multiply_value, 'wo')
                            if show_legend:
                                a.legend()

                    if line_4:
                        a.plot(x, temp_f, chosen_color_4, label='Fahrenheit')

                        a_2.fill_between(x, temp_f_min, temp_f, facecolor='#00ffe8', alpha=.5)
                        if show_legend:
                            a.legend()

                        if line_sma:
                            ap2 = moving_average(temp_f, period)
                            a.plot(x[len(x) - len(ap2):], ap2, 'y--', label='SMA')
                            a_2.plot(ap2, 'y--')
                            if show_legend:
                                a.legend()

                        if line_scaled:
                            multiply_value = scale_lines(temp_f, multiplier)
                            a.plot(x, multiply_value, 'g--', label='Scalled line')
                            a_2.plot(multiply_value, 'g--')
                            if show_legend:
                                a.legend()

                    if line_5:
                        a.plot(x, stan, chosen_color_5, label='State')

                        a_2.fill_between(x, stan_min, stan, facecolor='#00ffe8', alpha=.5)
                        if show_legend:
                            a.legend()

                        if line_sma:
                            ap2 = moving_average(stan, period)
                            a.plot(x[len(x) - len(ap2):], ap2, 'y--', label='SMA')
                            a_2.plot(ap2, 'y--')
                            if show_legend:
                                a.legend()

                        if line_scaled:
                            multiply_value = scale_lines(stan, multiplier)
                            a.plot(x, multiply_value, 'bo', label='Scalled line')
                            a_2.plot(multiply_value, 'bo')
                            if show_legend:
                                a.legend()

                    for label in a_2.xaxis.get_ticklabels():
                        label.set_rotation(45)

                except Exception as e1:
                    print(e1)

            except Exception as e2:
                print(e2)

        if picked_choice == 'random':
            f.clf()
            try:
                a = plt.subplot2grid((5, 4), (0, 0), rowspan=4, colspan=4, axisbg='#07000d')
                a_2 = plt.subplot2grid((5, 4), (4, 0), sharex=a, rowspan=1, colspan=4, axisbg=bg_color)

                a.grid(b=show_grid, color='w')
                a.yaxis.label.set_color('w')
                a.spines['bottom'].set_color('#5998ff')
                a.spines['top'].set_color('#5998ff')
                a.spines['left'].set_color('#5998ff')
                a.spines['right'].set_color('#5998ff')
                a.tick_params(axis='y', colors='w')
                a.xaxis.set_major_locator(mticker.MaxNLocator(10))
                plt.ylabel('Net Data')

                pd.options.mode.chained_assignment = None  # panda error skipped
                data_link = r'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
                data = urllib.request.urlopen(data_link)
                data = data.readall().decode('utf-8')
                data = json.loads(data)

                data = data['btc_usd']
                data = pd.DataFrame(data)

                buys = data[(data['type'] == 'bid')]
                buys['datestamp'] = np.array(buys['timestamp']).astype('datetime64[s]')
                buy_dates = (buys['datestamp']).tolist()

                sells = data[(data['type'] == 'ask')]
                sells['datestamp'] = np.array(sells['timestamp']).astype('datetime64[s]')
                sell_dates = (sells['datestamp']).tolist()

                a.clear()

                a.plot_date(buy_dates, buys['price'], 'g', label='buy')
                a.plot_date(sell_dates, sells['price'], 'r', label='sell')

                if show_legend:
                    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)

                title_ = 'Last value ' + str(data['price'][1999])
                a.set_title(title_)
                a.grid(show_grid)

            except Exception as e:
                ser_mod.popup_msg(e)


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='''
    Arduino - port monitor.
    Data might not be accurate.
    Using at your own risk.
    ''', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Nie zgadzam się', command=quit)  # podajemy parametr i zapętlamy
        button1.pack()

        button2 = ttk.Button(self, text='Zgadzam się',
                             command=lambda: controller.show_frame(PageOne))  # podajemy parametr i zapętlamy
        button2.pack()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Choose data source', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text='Exit', command=quit)  #
        button.pack()

        button2 = ttk.Button(self, text='Arduino Data',
                             command=lambda: controller.show_frame(PageOne))  #
        button2.pack()

        button3 = ttk.Button(self, text='Random',
                             command=lambda: controller.show_frame(PageTwo))  #
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Configuring page',
                             command=lambda: controller.show_frame(StartPage))  # 
        # button1.pack ()

        button2 = ttk.Button(self, text='Exit',
                             command=quit)
        # button2.pack ()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()

        # MatPlotLib toolbar to chart
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()

        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Random route', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Configuring page',
                             command=lambda: controller.show_frame(StartPage))  #
        button1.pack()

        button2 = ttk.Button(self, text='Exit',
                             command=quit)  #
        button2.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()

        # MatPlotLib toolbar to window.
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()

        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# global ani2

app = Main()
app.geometry('1024x768')  # app window default resolution
# set_interval(DRAWING_INTERVAL)   # default refreshing frequency
# ad = Thread(target=set_interval, args=(),).start()
ani2 = animation_plt.FuncAnimation(f, graph_data, frames=10, interval=set_interval(interval))
# ad = Thread(target=set_interval(DRAWING_INTERVAL), args=(),).start()
app.mainloop()
