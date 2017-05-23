"""
Module creating main menu
"""

# from PyQt5 import QtCore, QtGui, QtWidgets
#
# __author__ = "Przemek"
#
#
# class BuildMenu(tk.Menu):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         tk.Tk.iconbitmap(self, default='ikona_orange.ico')
#         tk.Tk.wm_title(self, 'main')
#
#         container = tk.Frame(self)
#         container.pack(side='top', fill='both', expand='True')
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         menu_bar = tk.Menu(container)
#         menu_file = tk.Menu(menu_bar, tearoff=0)  # unfixed menu
#         menu_file.add_command(label='Save log with raw data... ', command=lambda: m_file.save_raw_file())
#         menu_file.add_separator()
#         menu_file.add_command(label='Exit', command=quit)
#         menu_bar.add_cascade(label='File..', menu=menu_file)
#
#         change_freq_menu = tk.Menu(menu_bar, tearoff=1)
#         port_menu = tk.Menu(menu_bar, tearoff=1)
#
#         menu_bar.add_cascade(label='Port...', menu=port_menu)
#         menu_bar.add_cascade(label='Cz�stotliwo��...', menu=change_freq_menu)
#
#         port_menu.add_command(label='Skonfiguruj port',
#                               command=lambda: ser_mod.set_port_spec())
#         port_menu.add_command(label="Czas", command=lambda: ser_mod.calculate_freq())
#
#         change_freq_menu.add_command(label='Czestotliwosc 100 ms',
#                                      command=lambda: m_file.set_interval('100ms'))
#         change_freq_menu.add_command(label='Czestotliwosc 200 ms',
#                                      command=lambda: m_file.set_interval('200ms'))
#         change_freq_menu.add_command(label='Czestotliwosc 500 ms',
#                                      command=lambda: m_file.set_interval('500ms'))
#         change_freq_menu.add_command(label='Czestotliwosc 600 ms',
#                                      command=lambda: m_file.set_interval('600ms'))
#         change_freq_menu.add_command(label='Czestotliwosc 1000 ms',
#                                      command=lambda: m_file.set_interval('1000ms'))
#         change_freq_menu.add_command(label='Czestotliwosc 3000 ms',
#                                      command=lambda: m_file.set_interval('3000ms'))
#         change_freq_menu.add_command(label='Czestotliwosc 5000 ms',
#                                      command=lambda: m_file.set_interval('5000ms'))
#
#         view_menu = tk.Menu(menu_bar, tearoff=1)
#         view_menu.add_command(label='X labels (On/Off)',
#                               command=lambda: m_file.show_elements('X_axis'))
#         view_menu.add_command(label='Y labels (On/Off)',
#                               command=lambda: m_file.show_elements('Y_axis'))
#         view_menu.add_command(label='Legenda (On/Off)',
#                               command=lambda: m_file.show_elements('Legenda'))
#         view_menu.add_command(label='Grid (On/Off)',
#                               command=lambda: m_file.show_elements('Grid'))
#         view_menu.add_command(label='Wszystko (On/Off)',
#                               command=lambda: m_file.show_elements('Wszystko'))
#         menu_bar.add_cascade(label='Widok', menu=view_menu)
#
#         data_gen_menu = tk.Menu(menu_bar, tearoff=1)
#         data_gen_menu.add_command(label='Rozpocznij generowanie danych z portu',
#                                   command=lambda: ser_mod.start_stop('startuj'))
#         data_gen_menu.add_command(label='Wykres - arduino',
#                                   command=lambda: m_file.choose_data_source('arduino'))
#         data_gen_menu.add_command(label='Filtruj Y', command=lambda: m_file.set_filter())
#
#         data_gen_menu.add_command(label='Skaluj dane...', command=lambda: m_file.set_period("Multiplier"))
#         data_gen_menu.add_command(label='Set SMA PERIOD...', command=lambda: m_file.set_period("SMA"))
#
#         menu_bar.add_cascade(label='Dane', menu=data_gen_menu)
#
#         resume_pause_menu = tk.Menu(menu_bar, tearoff=1)
#         resume_pause_menu.add_command(label='Resume',
#                                       command=lambda: ser_mod.start_stop('startuj'))
#         resume_pause_menu.add_command(label='Pause',
#                                       command=lambda: ser_mod.start_stop('stopuj'))
#
#         menu_bar.add_cascade(label='Resume/Stop', menu=resume_pause_menu)
#
#         bg_style_menu = tk.Menu(menu_bar, tearoff=1)  # list of available styles
#         style_menu = tk.Menu(menu_bar, tearoff=1)  # list of
#         bg_menu = tk.Menu(menu_bar, tearoff=1)  #
#
#         menu_bar.add_cascade(label="Zmie� styl rysowania", menu=bg_style_menu)
#
#         bg_style_menu.add_cascade(label="Style", menu=style_menu)
#         bg_style_menu.add_cascade(label="Background...", menu=bg_menu)
#
#         bg_menu.add_command(label='Bia�e t�o wykresu', command=lambda: m_file.bg_set('white'))
#         bg_menu.add_command(label='Szare t�o wykresu', command=lambda: m_file.bg_set('grey'))
#         bg_menu.add_command(label='��te t�o wykresu', command=lambda: m_file.bg_set('yellow'))
#         bg_menu.add_command(label='Niebieskie t�o wykresu', command=lambda: m_file.bg_set('blue'))
#         bg_menu.add_command(label='Odcienie szaro�ci', command=lambda: m_file.bg_set('grayscale'))
#
#         style_menu.add_command(label='Styl Dark Background', command=lambda: m_file.bg_set('dark_background'))
#         style_menu.add_command(label='Styl ggplot', command=lambda: m_file.bg_set('ggplot'))
#         style_menu.add_command(label='Styl fivethirtyeight', command=lambda: m_file.bg_set('fivethirtyeight'))
#         style_menu.add_command(label='Styl bmh', command=lambda: m_file.bg_set('bmh'))
#
#         set_lines_menu = tk.Menu(menu_bar, tearoff=1)
#         set_lines_menu.add_command(label='Linia 1', command=lambda: m_file.print_lines('line1'))
#         set_lines_menu.add_command(label='Linia 2', command=lambda: m_file.print_lines('line2'))
#         set_lines_menu.add_command(label='Linia 3', command=lambda: m_file.print_lines('line3'))
#         set_lines_menu.add_command(label='Linia 4', command=lambda: m_file.print_lines('line4'))
#         set_lines_menu.add_command(label='Linia 5', command=lambda: m_file.print_lines('line5'))
#         set_lines_menu.add_command(label='SMA', command=lambda: m_file.print_lines('linia_sma'))
#         set_lines_menu.add_command(label="Scaled", command=lambda: m_file.print_lines('LINE_SCALED_FLAG'))
#         set_lines_menu.add_command(label="Optimized", command=lambda: m_file.print_lines('LINE_OPTIMIZED_FLAG'))
#
#         menu_bar.add_cascade(label='W��cz linie', menu=set_lines_menu)
#
#         change_color_menu = tk.Menu(menu_bar, tearoff=1)
#         change_line_color = tk.Menu(menu_bar, tearoff=1)
#
#         change_line_color.add_command(label='Niebieski', command=lambda: m_file.set_lines_color('blue'))
#         change_line_color.add_command(label='Bia�y', command=lambda: m_file.set_lines_color('white'))
#         change_line_color.add_command(label='W�asny', command=lambda: m_file.set_lines_color('wlasny'))
#         change_line_color.add_command(label='R�owy', command=lambda: m_file.set_lines_color('pink'))
#         change_line_color.add_command(label='Zielony', command=lambda: m_file.set_lines_color('green'))
#         change_line_color.add_command(label='Z�ty', command=lambda: m_file.set_lines_color('yellow'))
#         change_line_color.add_command(label='Czerwony', command=lambda: m_file.set_lines_color('red'))
#
#         menu_bar.add_cascade(label='Zmien kolor linii', menu=change_color_menu)
#
#         change_color_menu.add_cascade(label='Linia 1', menu=change_line_color)
#         change_color_menu.add_cascade(label='Linia 2', menu=change_line_color)
#         change_color_menu.add_cascade(label='Linia 3', menu=change_line_color)
#         change_color_menu.add_cascade(label='Linia 4', menu=change_line_color)
#         change_color_menu.add_cascade(label='Linia 5', menu=change_line_color)
#
#         author_menu = tk.Menu(menu_bar, tearoff=0)
#         author_menu.add_command(label='Info', command=lambda: ser_mod.popup_msg())
#
#         menu_bar.add_cascade(label='O autorze', menu=author_menu)
#
#         tk.Tk.config(self, menu=menu_bar)
#
#         self.frames = {}
#
#         # List of pages in an app
#         for f in {HomePage, StartPage}:
#             frame = f(container, self)
#
#             self.frames[f] = frame
#
#             frame.grid(row=0, column=0, sticky='nsew')  # north side east west
