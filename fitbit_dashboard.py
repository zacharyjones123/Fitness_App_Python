from data import Date
import csv

dates = []
with open('full20191001.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        try:
            new_date = Date(row[0], float(row[1]), float(row[2]), float(row[3]))
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

    total = 0
    for i in range(7):
        total += dates_array[len(dates_array)-i-1].get_weight()
    print("Weight: ", total/7)

    total = 0
    for i in range(7):
        total += dates_array[len(dates_array)-i-1].get_calories()
    print("Calories: ", total/7)

average_last_7_days(dates)