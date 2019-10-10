import tkinter as tk
from tkinter import ttk
import csv
from data import Date
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


LARGE_FONT = ("Verdana", 12)


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Fitbit Dashboard")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RunningPage, NutritionPage, DashboardPage, StatisticsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StatisticsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Body Fat Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        ##### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots(2, 2)

        for tick in axs[0,0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        bodyfat_array = Date.dates_to_bodyfat_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0,0].set_title('Body Fat')
        axs[0,0].set_xlabel('Time')
        axs[0,0].set_ylabel('Body Fat')
        axs[0,0].plot_date(dates1, bodyfat_array, 'b-')

        ##### Plot (0,1) - Calories Plot - #####
        for tick in axs[0,1].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        calories_array = Date.dates_to_calories_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 1].set_title('Calories')
        axs[0, 1].set_xlabel('Time')
        axs[0, 1].set_ylabel('Calories')
        axs[0, 1].plot_date(dates1, calories_array, 'b-')

        # top line 3000 calories
        axs[0, 1].axhline(y=3000, color='r', linestyle='-')
        axs[0, 1].axhline(y=2750, color='g', linestyle='-')
        axs[0, 1].axhline(y=2500, color='b', linestyle='-')

        ##### Plot (1,0) - Weight Plot - #####
        for tick in axs[1,0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        weight_array = Date.dates_to_weight_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[1, 0].set_title('Weight')
        axs[1, 0].set_xlabel('Time')
        axs[1, 0].set_ylabel('Weight')
        axs[1, 0].plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Running Page",
                             command=lambda: controller.show_frame(RunningPage))
        button2.pack()

        button3 = ttk.Button(self, text="Nutrition Page",
                             command=lambda: controller.show_frame(NutritionPage))
        button3.pack()

        button4 = ttk.Button(self, text="Dashboard Page",
                             command=lambda: controller.show_frame(DashboardPage))
        button4.pack()

        button5 = ttk.Button(self, text="Statistics Page",
                             command=lambda: controller.show_frame(StatisticsPage))
        button5.pack()


class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Dashboard Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        ##### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots(2, 2)

        for tick in axs[0, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        bodyfat_array = Date.dates_to_bodyfat_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 0].set_title('Body Fat')
        axs[0, 0].set_xlabel('Time')
        axs[0, 0].set_ylabel('Body Fat')
        axs[0, 0].plot_date(dates1, bodyfat_array, 'b-')

        ##### Plot (0,1) - Calories Plot - #####
        for tick in axs[0, 1].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        calories_array = Date.dates_to_calories_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 1].set_title('Calories')
        axs[0, 1].set_xlabel('Time')
        axs[0, 1].set_ylabel('Calories')
        axs[0, 1].plot_date(dates1, calories_array, 'b-')

        # top line 3000 calories
        axs[0, 1].axhline(y=3000, color='r', linestyle='-')
        axs[0, 1].axhline(y=2750, color='g', linestyle='-')
        axs[0, 1].axhline(y=2500, color='b', linestyle='-')

        ##### Plot (1,0) - Weight Plot - #####
        for tick in axs[1, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        weight_array = Date.dates_to_weight_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[1, 0].set_title('Weight')
        axs[1, 0].set_xlabel('Time')
        axs[1, 0].set_ylabel('Weight')
        axs[1, 0].plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class RunningPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Running Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        ##### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots(2, 2)

        for tick in axs[0, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        bodyfat_array = Date.dates_to_bodyfat_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 0].set_title('Body Fat')
        axs[0, 0].set_xlabel('Time')
        axs[0, 0].set_ylabel('Body Fat')
        axs[0, 0].plot_date(dates1, bodyfat_array, 'b-')

        ##### Plot (0,1) - Calories Plot - #####
        for tick in axs[0, 1].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        calories_array = Date.dates_to_calories_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 1].set_title('Calories')
        axs[0, 1].set_xlabel('Time')
        axs[0, 1].set_ylabel('Calories')
        axs[0, 1].plot_date(dates1, calories_array, 'b-')

        # top line 3000 calories
        axs[0, 1].axhline(y=3000, color='r', linestyle='-')
        axs[0, 1].axhline(y=2750, color='g', linestyle='-')
        axs[0, 1].axhline(y=2500, color='b', linestyle='-')

        ##### Plot (1,0) - Weight Plot - #####
        for tick in axs[1, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        weight_array = Date.dates_to_weight_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[1, 0].set_title('Weight')
        axs[1, 0].set_xlabel('Time')
        axs[1, 0].set_ylabel('Weight')
        axs[1, 0].plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class NutritionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Nutrition Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        ##### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots(2, 2)

        for tick in axs[0, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        bodyfat_array = Date.dates_to_bodyfat_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 0].set_title('Body Fat')
        axs[0, 0].set_xlabel('Time')
        axs[0, 0].set_ylabel('Body Fat')
        axs[0, 0].plot_date(dates1, bodyfat_array, 'b-')

        ##### Plot (0,1) - Calories Plot - #####
        for tick in axs[0, 1].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        calories_array = Date.dates_to_calories_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 1].set_title('Calories')
        axs[0, 1].set_xlabel('Time')
        axs[0, 1].set_ylabel('Calories')
        axs[0, 1].plot_date(dates1, calories_array, 'b-')

        # top line 3000 calories
        axs[0, 1].axhline(y=3000, color='r', linestyle='-')
        axs[0, 1].axhline(y=2750, color='g', linestyle='-')
        axs[0, 1].axhline(y=2500, color='b', linestyle='-')

        ##### Plot (1,0) - Weight Plot - #####
        for tick in axs[1, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Date.dates_to_dates_array(get_dates_array())
        weight_array = Date.dates_to_weight_array(get_dates_array())
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[1, 0].set_title('Weight')
        axs[1, 0].set_xlabel('Time')
        axs[1, 0].set_ylabel('Weight')
        axs[1, 0].plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

def get_dates_array():
    dates = []
    with open('data/full/full2019-10-08.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            try:
                new_date = Date(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]),float(row[6]), float(row[7]), float(row[8]))
                dates.append(new_date)
            except ValueError:
                print("This is fine, just need to skip first row")
    return dates

app = MainWindow()
app.mainloop()
