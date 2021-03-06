import tkinter as tk
from tkinter import ttk
import csv
from tools.data import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

matplotlib.use("TkAgg")


LARGE_FONT = ("Verdana", 12)


def get_dates_array():
    dates = []
    with open('../data/full/full2019-10-08.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')

        for row in readcsv:
            try:
                new_date = Nutrition(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]),
                                float(row[6]), float(row[7]), float(row[8]))
                dates.append(new_date)
            except ValueError:
                pass
                # print("This is fine, just need to skip first row")
    return dates

def get_workout_data():
    workouts = []
    with open('../data/weight_training/weight_training2019-10-15.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')

        for row in readcsv:
            try:
                new_date = WeightTraining(row[0], "First Workout", row[1], row[2], row[3], row[4], row[5], row[6])
                workouts.append(new_date)
            except ValueError:
                pass
                # print("This is fine, just need to skip first row")
    return workouts


dates_array = get_dates_array()


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

        for F in (DashboardPage, RunningPage, NutritionPage, WeightTrainingPage, HeartRatePage, SleepingPage, CompetitionsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0 , column=0, sticky="nsew")

        # (1) First Frame of the GUI
        # This is the beginning page
        self.show_frame(WeightTrainingPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StatisticsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Body Fat Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # #### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots(2, 2)

        for tick in axs[0, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        bodyfat_array = Data.dates_to_bodyfat_array(dates_array)
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 0].set_title('Body Fat')
        axs[0, 0].set_xlabel('Time')
        axs[0, 0].set_ylabel('Body Fat')
        axs[0, 0].plot_date(dates1, bodyfat_array, 'b-')

        # #### Plot (0,1) - Calories Plot - #####
        for tick in axs[0, 1].get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        calories_array = Data.dates_to_calories_array(dates_array)
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

        # #### Plot (1,0) - Weight Plot - #####
        for tick in axs[1, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        weight_array = Data.dates_to_weight_array(dates_array)
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
        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class DashboardPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Daily Page", font=LARGE_FONT)
        label.grid(row = 0, column=1,pady=10, padx=10)

        frame_top_left = DailyPage(self, controller)
        frame_top_left.grid(row=0, column=0)

        frame_top_right = WeightPage(self, controller)
        frame_top_right.grid(row=0, column=1)

        frame_bottom_left = CaloriesPage(self, controller)
        frame_bottom_left.grid(row=1, column=0)

        frame_bottom_right = TodoPage(self, controller)
        frame_bottom_right.grid(row=1, column=1)

        # The right buttom to go to the Running frame
        button_right_bottom = tk.Button(self, text="Next->",
                                        command=lambda: controller.show_frame(RunningPage))
        button_right_bottom.grid(column=2, columnspan=2, row=0)

        button8 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(DashboardPage))
        button8.grid(row=2, rowspan=2)


class DailyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)

        label = tk.Label(self, text="Daily Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_weight = tk.Label(self, text="327.4 lbs", font=LARGE_FONT)
        label_weight.pack(pady=10, padx=10)
        label_bodyfat = tk.Label(self, text="39.0 %BF", font=LARGE_FONT)
        label_bodyfat.pack(pady=10, padx=10)
        label_calories = tk.Label(self, text="2541 cal", font=LARGE_FONT)
        label_calories.pack(pady=10, padx=10)
        label_streak = tk.Label(self, text="40 day streak", font=LARGE_FONT)
        label_streak.pack(pady=10, padx=10)
        label_steps = tk.Label(self, text="10000 steps", font=LARGE_FONT)
        label_steps.pack(pady=10, padx=10)


class WeightPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Weight Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # #### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots()

        # #### Plot (1,0) - Weight Plot - #####
        for tick in axs.get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        weight_array = Nutrition.dates_to_weight_array(dates_array)
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs.set_title('Weight')
        axs.set_xlabel('Time')
        axs.set_ylabel('Weight')
        axs.plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class CaloriesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Calories Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # #### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots()

        # #### Plot (1,0) - Weight Plot - #####
        for tick in axs.get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        calories_array = Nutrition.dates_to_calories_array(dates_array)
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs.set_title('Calories')
        axs.set_xlabel('Time')
        axs.set_ylabel('Calories')
        axs.plot_date(dates1, calories_array, 'b-')

        # top line 3000 calories
        axs.axhline(y=3000, color='r', linestyle='-')
        axs.axhline(y=2750, color='g', linestyle='-')
        axs.axhline(y=2500, color='b', linestyle='-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class TodoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Todo Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_weight = tk.Label(self, text="327.4 lbs", font=LARGE_FONT)
        label_weight.pack(pady=10, padx=10)
        label_bodyfat = tk.Label(self, text="39.0 %BF", font=LARGE_FONT)
        label_bodyfat.pack(pady=10, padx=10)
        label_calories = tk.Label(self, text="2541 cal", font=LARGE_FONT)
        label_calories.pack(pady=10, padx=10)
        label_streak = tk.Label(self, text="40 day streak", font=LARGE_FONT)
        label_streak.pack(pady=10, padx=10)
        label_steps = tk.Label(self, text="10000 steps", font=LARGE_FONT)
        label_steps.pack(pady=10, padx=10)


class RunningPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Running Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # #### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots()

        # #### Plot (1,0) - Weight Plot - #####
        for tick in axs.get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        weight_array = Nutrition.dates_to_weight_array(dates_array)
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs.set_title('Weight')
        axs.set_xlabel('Time')
        axs.set_ylabel('Weight')
        axs.plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # The right buttom to go to the Nutrition frame
        button_next = tk.Button(self, text="Next->",
                                command=lambda: controller.show_frame(NutritionPage))
        button_next.pack(pady=10, padx=10)

        # The left buttom to go to the Dashboard frame
        button_back = tk.Button(self, text="<-Prev>",
                                command=lambda: controller.show_frame(DashboardPage))
        button_back.pack(pady=10, padx=10)

        button8 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(DashboardPage))
        button8.pack()


class NutritionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Body Fat Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # #### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots(2, 2)

        for tick in axs[0, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        bodyfat_array = Nutrition.dates_to_bodyfat_array(dates_array)
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs[0, 0].set_title('Body Fat')
        axs[0, 0].set_xlabel('Time')
        axs[0, 0].set_ylabel('Body Fat')
        axs[0, 0].plot_date(dates1, bodyfat_array, 'b-')

        # #### Plot (0,1) - Calories Plot - #####
        for tick in axs[0, 1].get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        calories_array = Nutrition.dates_to_calories_array(dates_array)
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

        # #### Plot (1,0) - Weight Plot - #####
        for tick in axs[1, 0].get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        weight_array = Nutrition.dates_to_weight_array(dates_array)
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
        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # The right buttom to go to the Nutrition frame
        button_next = tk.Button(self, text="Next->",
                                command=lambda: controller.show_frame(WeightTrainingPage))
        button_next.pack(pady=10, padx=10)

        # The left buttom to go to the Dashboard frame
        button_back = tk.Button(self, text="<-Prev>",
                                command=lambda: controller.show_frame(RunningPage))
        button_back.pack(pady=10, padx=10)

        button8 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(DashboardPage))
        button8.pack()


class WeightTrainingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Weight Training Page", font=LARGE_FONT)
        label.grid(row=0, column=1, columnspan=2, pady=10, padx=10)
        
        workout_data = get_workout_data()

        # Let's show some basic data
        left_canvas = tk.Canvas(self)
        scroll_y = tk.Scrollbar(self, orient="vertical", command=left_canvas.yview)

        left_frame = tk.Frame(left_canvas, highlightbackground="black", highlightthickness=1)

        for i in range(len(workout_data)):
            first_label = tk.Label(left_frame, text=str(workout_data[i]), font=LARGE_FONT, relief="groove", borderwidth=2)
            first_label.pack()

        left_canvas.create_window(0, 0, anchor='nw', window=left_frame)

        left_canvas.update_idletasks()
        left_canvas.configure(scrollregion=left_canvas.bbox('all'),
                              yscrollcommand=scroll_y.set)
        left_canvas.grid(row=1, column=0, pady=10, padx=10)
        scroll_y.grid(row=1, column=1, sticky="ns")
        center_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        center_label = tk.Label(center_frame, text="Trends", font=LARGE_FONT)
        center_label.pack()
        center_frame.grid(row=1, column=2, pady=10, padx=10)
        right_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        right_label = tk.Label(right_frame, text="Overall", font=LARGE_FONT)
        right_label.pack()
        right_frame.grid(row=1, column=3, pady=10, padx=10)
        # The right buttom to go to the Nutrition frame
        button_next = tk.Button(self, text="Next->",
                                command=lambda: controller.show_frame(HeartRatePage))
        button_next.grid(row=2, column=1, columnspan=2, pady=10, padx=10)

        # The left buttom to go to the Dashboard frame
        button_back = tk.Button(self, text="<-Prev>",
                                command=lambda: controller.show_frame(NutritionPage))
        button_back.grid(row=3, column=1, columnspan=2, pady=10, padx=10)

        button8 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(DashboardPage))
        button8.grid(row=4, column=1, columnspan=2, pady=10, padx=10)


class HeartRatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Heart Rate Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # #### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots()

        # #### Plot (1,0) - Weight Plot - #####
        for tick in axs.get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        weight_array = Nutrition.dates_to_weight_array(dates_array)
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs.set_title('Weight')
        axs.set_xlabel('Time')
        axs.set_ylabel('Weight')
        axs.plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # The right buttom to go to the Nutrition frame
        button_next = tk.Button(self, text="Next->",
                                command=lambda: controller.show_frame(SleepingPage))
        button_next.pack(pady=10, padx=10)

        # The left buttom to go to the Dashboard frame
        button_back = tk.Button(self, text="<-Prev>",
                                command=lambda: controller.show_frame(WeightTrainingPage))
        button_back.pack(pady=10, padx=10)

        button8 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(DashboardPage))
        button8.pack()


class SleepingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Sleeping Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # #### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots()

        # #### Plot (1,0) - Weight Plot - #####
        for tick in axs.get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        weight_array = Nutrition.dates_to_weight_array(dates_array)
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs.set_title('Weight')
        axs.set_xlabel('Time')
        axs.set_ylabel('Weight')
        axs.plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # The right buttom to go to the Nutrition frame
        button_next = tk.Button(self, text="Next->",
                                command=lambda: controller.show_frame(CompetitionsPage))
        button_next.pack(pady=10, padx=10)

        # The left buttom to go to the Dashboard frame
        button_back = tk.Button(self, text="<-Prev>",
                                command=lambda: controller.show_frame(HeartRatePage))
        button_back.pack(pady=10, padx=10)

        button8 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(DashboardPage))
        button8.pack()


class CompetitionsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Competitions Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Running Page",
                             command=lambda: controller.show_frame(RunningPage))
        button2.pack()

        button3 = ttk.Button(self, text="Nutrition Page",
                             command=lambda: controller.show_frame(NutritionPage))
        button3.pack()

        button4 = ttk.Button(self, text="Weight Training Page",
                             command=lambda: controller.show_frame(WeightTrainingPage))
        button4.pack()

        button5 = ttk.Button(self, text="Heart Rate Page",
                             command=lambda: controller.show_frame(HeartRatePage))
        button5.pack()

        button6 = ttk.Button(self, text="Sleeping Page",
                             command=lambda: controller.show_frame(SleepingPage))
        button6.pack()

        button8 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(DailyPage))
        button8.pack()
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)
        label = tk.Label(self, text="Competitions Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # #### Plot (0,0) - Body Fat Plot - #####
        fig, axs = plt.subplots()

        # #### Plot (1,0) - Weight Plot - #####
        for tick in axs.get_xticklabels():
            tick.set_rotation(45)

        time_array = Data.dates_to_dates_array(dates_array)
        weight_array = Nutrition.dates_to_weight_array(dates_array)
        # create figure and axis
        # set title and labels
        dates1 = matplotlib.dates.date2num(time_array)
        axs.set_title('Weight')
        axs.set_xlabel('Time')
        axs.set_ylabel('Weight')
        axs.plot_date(dates1, weight_array, 'b-')

        # This line is to keep the graphs from overlapping
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # The left buttom to go to the Dashboard frame
        button_back = tk.Button(self, text="<-Prev>",
                                command=lambda: controller.show_frame(SleepingPage))
        button_back.pack(pady=10, padx=10)

        button8 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(DashboardPage))
        button8.pack()


app = MainWindow()
app.mainloop()
