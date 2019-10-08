class Date:
    def __init__(self, time, bodyFat, weight, calories, carbs, fat, fiber, protein, sodium):
        self.time = time
        self.bodyFat = bodyFat
        self.weight = weight
        self.calories = calories
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.protein = protein
        self.sodium = sodium

    def get_time(self):
        return self.time

    def get_bodyFat(self):
        return self.fat

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

    def set_bodyFat(self, fat):
        self.fat = fat

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

    def __str__(self):
        return '%s : %s : %s : %s : %s : %s : %s : %s : %s' % (self.time, self.fat, self.weight, self.calories, self.carbs, self.fat, self.fiber, self.protein, self.sodium)
