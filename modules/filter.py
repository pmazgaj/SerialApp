"""
Handle behaviour of data filters
"""
import threading
from functools import reduce

__author__ = "Przemek"


class Filter(threading.Thread):
    def __init__(self, data, out):
        threading.Thread.__init__(self)
        self.data = data
        self.out = out
        self.jump = 1
        self.multiplier = 2
        self.period = 2  # splitter...
        self.weights = 0
        self.new_data_set = []
        self.a = []
        self.val1 = []
        self.val2 = []
        self.val3 = []
        self.val4 = []
        self.val5 = []
        self.val6 = []
        self.logfile = open('log.txt', 'a')

    def run(self):
        file = open(self.out, "a")

        file.write(str(self.data_scale(self.multiplier)))

        file.close()
        time.sleep(0.005)

    def data_scale(self, multiplier):
        self.multiplier = multiplier  # setting up MULTIPLIER
        a = [[], [], [], [], [], [], []]
        g = [[], [], [], [], [], [], []]  # Lista na siedem list danych z arduino
        for i, value in enumerate(self.data.split(" ")):
            a[i].append(float(value) * self.multiplier)
        return str(a).replace('[', '').replace(']', '').replace(',', '') + "\n"

    def unique_values(self):  #
        seen = set()  # set...
        for i, value in enumerate(self.data.split(' ')):
            self.a.append(value)
            values_list = []
            if (len(self.a)) >= 7:
                q, w, e, r, t, y, m = self.a
                values_list.extend((q, w, e, r, t, y))

                print(set(values_list))
            if value not in seen:
                yield value
                seen.add(value)

    def raw_data(self):
        self.logfile.write(str(data))
        self.logfile.close()


def timer():
    calc_time = time.clock()
    return int(calc_time)


def calculate_freq():
    if timer() > 0:
        sample_time.append(timer() / data_count)

        def average_value(values):
            simple_average = sum(values) / len(values)
            return simple_average

        avg_t = average_value(sample_time)
        freq.append(1 / avg_t)

        if avg_t <= sample_time[-1]:
            pass

        else:
            print("maly")

        avg_freq = average_value(freq)
        nyquist_freq = (0.5 * freq[-1])

        popup_msg("Czas całkowity: {} s\n"
                  "Czas obecnej próbki: {:.3} s\n"
                  "Średni czas próbkowania: {:.3} s\n"
                  "Częstotliwość: {:.3} Hz\n"
                  "Średnia częstotliwość: {:.3} Hz\n"
                  "Nyquist : {:.3} Hz".format(timer(), sample_time[-1], avg_t, freq[-1], avg_freq, nyquist_freq))


def main():
    t1 = Filter(data, 'log_raw.txt')
    t2 = Filter(data, 'log_skaluj.txt')
    t3 = Filter(data, 'log_srednia_kroczaca.txt')
    t4 = Filter(data, 'log_unique.txt')
    t5 = Filter(data, 'log_t5.txt')
    t.append(t1)
    t.append(t2)
    t.append(t3)
    t.append(t4)
    t.append(t5)

    if IS_REFRESHING is False:
        for each_thread in t:
            each_thread.stop()

    elif IS_REFRESHING is True:
        t1.raw_data()

    else:
        popup_msg("CONDOMINIUM GERMAN-RUSSIAN UNDER ESTIMATE OF JEWISH LEAD")


def open_file():
    try:
        main()

    except Exception as exception2:
        return exception2


def file_exists(path_given):  # usuniecie pliku, na poczatku działania
    if os.path.isfile(path_given):
        os.unlink(path_given)
    else:
        pass


def change_granularity(x, y, divider):
    gran_x = x
    gran_y = y

    changed_gran_x = []
    changed_gran_y = []

    g_x = len(x)
    while g_x > divider:
        x_list = gran_x[g_x - divider:g_x]
        x_avg = reduce(lambda x, y: x + y, x_list) / float(len(x_list))

        y_list = gran_y[g_x - divider:g_x]
        y_avg = reduce(lambda x, y: x + y, y_list) / float(len(y_list))

        changed_gran_x.append(x_avg)
        changed_gran_y.append(y_avg)

        g_x -= divider

        # print(changed_gran_x)
        # print(changed_gran_y)
        return changed_gran_x, changed_gran_y
