# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk

import csv
from tools.data import Date

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Sea of BTC client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, BodyFatPage, WeightPage, CaloriesPage):
            frame = F(container, self)

            self.frames[F] = frame

            if F is StartPage:
                frame.grid(row=0, column=0, sticky="nsew")
            elif F is BodyFatPage:
                frame.grid(row=0, column=1, sticky="nsew")
            elif F is WeightPage:
                frame.grid(row=1, column=0, sticky="nsew")
            elif F is CaloriesPage:
                frame.grid(row=1, column=1, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        for tick in a.get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        calories_array = Date.dates_to_bodyfat_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        a.plot_date(dates1, calories_array, 'b-')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class BodyFatPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        for tick in a.get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        calories_array = Date.dates_to_bodyfat_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        a.plot_date(dates1, calories_array, 'b-')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class WeightPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        for tick in a.get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        calories_array = Date.dates_to_weight_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        a.plot_date(dates1, calories_array, 'b-')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class CaloriesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        for tick in a.get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        calories_array = Date.dates_to_calories_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        a.plot_date(dates1, calories_array, 'b-')

        # top line 3000 calories
        a.axhline(y=3000, color='r', linestyle='-')
        a.axhline(y=2750, color='g', linestyle='-')
        a.axhline(y=2500, color='b', linestyle='-')

        # bottom line 2500 calories

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def get_dates_array():
    dates = []
    with open('../data/full/full2019-10-08.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            try:
                new_date = Date(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]),float(row[6]), float(row[7]), float(row[8]))
                dates.append(new_date)
            except ValueError:
                print("This is fine, just need to skip first row")
    return dates

app = SeaofBTCapp()
app.mainloop()