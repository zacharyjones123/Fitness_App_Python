class Date:
    def __init__(self, time, fat, weight, calories):
        self.time = time
        self.fat = fat
        self.weight = weight
        self.calories = calories

    def get_time(self):
        return self.time

    def get_fat(self):
        return self.fat

    def get_weight(self):
        return self.weight

    def get_calories(self):
        return self.calories

    def set_time(self, time):
        self.time = time

    def set_fat(self, fat):
        self.fat = fat

    def set_weight(self, weight):
        self.weight = weight

    def set_calories(self, calories):
        self.calories = calories

    def __str__(self):
        return '%s : %s : %s' % (self.time, self.fat, self.weight)
