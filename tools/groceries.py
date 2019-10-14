import csv

class FoodLion:
    def __init__(self, name, cost, category):
        self.name = name
        self.cost = cost
        self.category = category

    def set_name(self, name):
        self.name = name

    def set_cost(self, cost):
        self.cost = cost

    def set_category(self, category):
        self.category = category

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_category(self):
        return self.category

    def __str__(self):
        s = ""
        s += "Name: " + self.name
        s += "\nCost: " + str(self.cost)
        s += "\nCategory: " + self.category
        s += "\n-----------------------------"
        return s


class Grocery(FoodLion):
    pass


class Produce(FoodLion):
    pass


def total_cost(items):
    total = 0
    for i in items:
        total += i.get_cost()
    return total

# Need to read in from the file
groceries = []
print("\n-----------------------------")

with open("../data/groceries/groceries.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        try:
            groceries.append(FoodLion(row[0], float(row[1]), row[2]))
        except ValueError:
            print("This is fine, just need to skip the first row")

for g in groceries:
    print(g)
print(total_cost(groceries))
