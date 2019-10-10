from datetime import datetime


class Date:
    def __init__(self, time, bodyfat, weight, calories, carbs, fat, fiber, protein, sodium):
        self.time = time
        self.bodyfat = bodyfat
        self.weight = weight
        self.calories = calories
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.protein = protein
        self.sodium = sodium

    def get_time(self):
        return self.time

    def get_bodyfat(self):
        return self.bodyfat

    def get_weight(self):
        return self.weight

    def get_calories(self):
        return self.calories

    def get_carbs(self):
        return self.carbs

    def get_fat(self):
        return self.fat

    def get_fiber(self):
        return self.fiber

    def get_protein(self):
        return self.protein

    def get_sodium(self):
        return self.sodium

    def set_time(self, time):
        self.time = time

    def set_bodyfat(self, bodyfat):
        self.bodyfat = bodyfat

    def set_weight(self, weight):
        self.weight = weight

    def set_calories(self, calories):
        self.calories = calories

    def set_carbs(self, carbs):
        self.carbs = carbs

    def set_fat(self, fat):
        self.fat = fat

    def set_fiber(self, fiber):
        self.fiber = fiber

    def set_protein(self, protein):
        self.protein = protein

    def set_sodium(self, sodium):
        self.sodium = sodium

    @staticmethod
    def dates_to_dates_array(dates_array):
        date_array = []
        for i in dates_array:
            date_array.append(datetime.strptime(i.get_time(), '%Y-%m-%d'))
        return date_array

    @staticmethod
    def dates_to_bodyfat_array(dates_array):
        bodyfat_array = []
        for i in dates_array:
            bodyfat_array.append(i.get_bodyfat())
        return bodyfat_array

    @staticmethod
    def dates_to_weight_array(dates_array):
        weight_array = []
        for i in dates_array:
            weight_array.append(i.get_weight())
        return weight_array

    @staticmethod
    def dates_to_calories_array(dates_array):
        calories_array = []
        for i in dates_array:
            calories_array.append(i.get_calories())
        return calories_array

    @staticmethod
    def dates_to_carbs_array(dates_array):
        carbs_array = []
        for i in dates_array:
            carbs_array.append(i.get_carbs())
        return carbs_array

    @staticmethod
    def dates_to_fat_array(dates_array):
        fat_array = []
        for i in dates_array:
            fat_array.append(i.get_fat())
        return fat_array

    @staticmethod
    def dates_to_fiber_array(dates_array):
        fiber_array = []
        for i in dates_array:
            fiber_array.append(i.get_fiber())
        return fiber_array

    @staticmethod
    def dates_to_protein_array(dates_array):
        protein_array = []
        for i in dates_array:
            protein_array.append(i.get_protein())
        return protein_array

    @staticmethod
    def dates_to_sodium_array(dates_array):
        sodium_array = []
        for i in dates_array:
            sodium_array.append(i.get_sodium())
        return sodium_array

    def __str__(self):
        return '%s : %s : %s : %s : %s : %s : %s : %s : %s' % (self.time, self.fat, self.weight, self.calories, self.carbs, self.fat, self.fiber, self.protein, self.sodium)
