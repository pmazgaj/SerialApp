"""
Create gui for setting serial port
"""

__author__ = "Przemek"


class SerialGui:
    def set_port_spec(self):
        try:
            self.ports_available()
        except ImportError:
        # self.popup_msg("Error while importing function")
        window_set_port = tk.Tk()
        path_ico = os.path.join(os.path.dirname(__file__), 'set_ico.ico')
        window_set_port.iconbitmap(default=path_ico)
        window_set_port.wm_title("Configuration window")
        window_set_port.geometry("240x320")

        label = ttk.Label(window_set_port, text="Wybor portu: ")
        label.pack(side="top", pady=10)

        var_ = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var6 = StringVar()

        combobox = ttk.Combobox(window_set_port, textvariable=var_)
        combobox.config(values=self.result)
        combobox.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Predkosc BAUD: ")
        label.pack(side="top", pady=0)

        combobox1 = ttk.Combobox(window_set_port, textvariable=var2)
        combobox1.config(values=(50, 75, 110, 134, 150,
                                 200, 300, 600, 1200,
                                 1800, 2400, 4800, 9600, 19200,
                                 38400, 57600, 115200))
        combobox1.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Data Bits: ")
        label.pack(side="top", pady=0)

        combobox2 = ttk.Combobox(window_set_port, textvariable=var3)
        combobox2.config(values=(5, 6, 7, 8))

        combobox2.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Parity : ")
        label.pack(side="top", pady=0)

        combobox3 = ttk.Combobox(window_set_port, textvariable=var4)
        combobox3.config(values=('None', 'Odd', 'Even', 'Mark', 'Space'))
        combobox3.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Stop Bits: ")
        label.pack(side="top", pady=0)

        combobox4 = ttk.Combobox(window_set_port, textvariable=var5)
        combobox4.config(values=(1, 1.5, 2))
        combobox4.pack(side="top", pady=0)

        label = ttk.Label(window_set_port, text="Flow control: ")
        label.pack(side="top", pady=0)

        combobox5 = ttk.Combobox(window_set_port, textvariable=var6)
        combobox5.config(values=('XON', 'X_OFF'))
        combobox5.pack(side="top", pady=0)

        def change_port_data():

            b_r = combobox1.get()
            c_n = combobox.get()
            d_b = combobox2.get()
            p_ = combobox3.get()
            s_b = combobox4.get()
            f_c = combobox5.get()

            self.baudrate1 = ''.join(x for x in b_r if x.isdigit())
            self.com_number = ''.join(x for x in c_n if x.isdigit())
            self.data_bits = ''.join(x for x in d_b if x.isdigit())
            self.parity = ''.join(x for x in p_)
            self.stop_bits = ''.join(x for x in s_b if x.isdigit())
            self.flow_control = ''.join(x for x in f_c)

            self.group.append(self.baudrate1)
            self.group.append(self.com_number)
            self.group.append(self.data_bits)
            self.group.append(self.parity)
            self.group.append(self.stop_bits)
            self.group.append(self.flow_control)

            print("Ustawiono : {}".format(self.group))

            print("Otworzono port {}".format(c_n))

            window_set_port.destroy()

        button1 = ttk.Button(window_set_port, text="Ustaw",
                             command=lambda: change_port_data())  # podajemy parametr i zapętlamy
        button1.pack()
