from tools.data import Date
import csv
import os

dates = []
with open('../data/full/full2019-10-08.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        try:
            new_date = Date(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]))
            dates.append(new_date)
        except ValueError:
            print("This is fine, just need to skip first row")


for temp in dates:
    print(temp)


# now to make methods for the data
def average_last_7_days(dates_array):
    print("Averages from dates: ")
    print("Beginning: ", dates_array[len(dates_array)-1])
    print("Ending: ", dates_array[len(dates_array)-8])
    print("----------------------")

    total_bodyFat = 0
    total_weight = 0
    total_calories = 0
    total_carbs = 0
    total_fat = 0
    total_fiber = 0
    total_protein = 0
    total_sodium = 0
    for i in range(7):
        total_bodyFat += dates_array[len(dates_array)-i-1].get_bodyfat()
        total_weight += dates_array[len(dates_array)-i-1].get_weight()
        total_calories += dates_array[len(dates_array)-i-1].get_calories()
        total_carbs += dates_array[len(dates_array)-i-1].get_carbs()
        total_fat += dates_array[len(dates_array)-i-1].get_fat()
        total_fiber += dates_array[len(dates_array)-i-1].get_fiber()
        total_protein += dates_array[len(dates_array)-i-1].get_protein()
        total_sodium += dates_array[len(dates_array)-i-1].get_sodium()
    print("Weight: ", total_weight/7)
    print("Body Fat: ", total_bodyFat/7)
    print("Calories: ", total_calories/7)
    print("Carbs: ", total_carbs/7)
    print("Fat: ", total_fat/7)
    print("Fiber: ", total_fiber/7)
    print("Protein: ", total_protein/7)
    print("Sodium: ", total_sodium/7)

average_last_7_days(dates)