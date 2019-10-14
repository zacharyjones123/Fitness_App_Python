from datetime import datetime


class Data:
    def __init__(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def __str__(self):
        return '%s' % self.time

    @staticmethod
    def dates_to_dates_array(dates_array):
        date_array = []
        for i in dates_array:
            date_array.append(datetime.strptime(i.get_time(), '%Y-%m-%d'))
        return date_array


class HeartRate(Data):
    def __init__(self, time, heart_rate_data):
        super().__init__(time)
        self.heart_rate_data = heart_rate_data

    def get_heart_rate_data(self):
        return self.heart_rate_data

    def set_heart_rate_data(self, heart_rate_data):
        self.heart_rate_data = heart_rate_data

    def __str__(self):
        return "HeartRate Data Structure"


class Sleep(Data):
    def __init__(self, time, sleep_data):
        super().__init__(time)
        self.sleep_data = sleep_data

    def get_sleep_data(self):
        return self.sleep_data

    def set_sleep_data(self, sleep_data):
        self.sleep_data = sleep_data

    def __str__(self):
        return "Sleep Data Structure"


class Nutrition(Data):
    def __init__(self, time, bodyfat, weight, calories, carbs, fat, fiber, protein, sodium):
        super().__init__(time)
        self.bodyfat = bodyfat
        self.weight = weight
        self.calories = calories
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.protein = protein
        self.sodium = sodium

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

    def __str__(self):
        return "Nutrition Data Structure"

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


class Workout(Data):
    def __init__(self, time, workout_name):
        super().__init__(time)
        self.workout_name = workout_name

    def get_workout_name(self):
        return self.workout_name

    def set_workout_name(self, workout_name):
        self.workout_name = workout_name

    def __str__(self):
        return "Workout Data Structure"


class WeightTraining(Workout):
    def __init__(self, time, workout_name, warm_up, exercise_name, set_num, reps, weight_used, rpe):
        super().__init__(time, workout_name)
        self.warm_up = warm_up
        self.exercise_name = exercise_name
        self.set_num = set_num
        self.reps = reps
        self.weight_used = weight_used
        self.rpe = rpe

    def get_warm_up(self):
        return self.warm_up

    def get_exercise_name(self):
        return self.exercise_name

    def get_set_num(self):
        return self.set_num

    def get_reps(self):
        return self.reps

    def get_weight_used(self):
        return self.weight_used

    def get_rpe(self):
        return self.rpe

    def set_warm_up(self, warm_up):
        self.warm_up = warm_up

    def set_exercise_name(self, exercise_name):
        self.exercise_name = exercise_name

    def set_set_num(self, set_num):
        self.set_num = set_num

    def set_reps(self, reps):
        self.reps = reps

    def set_weight_used(self, weight_used):
        self.weight_used = weight_used

    def set_rpe(self, rpe):
        self.rpe = rpe

    def __str__(self):
        return "Exercise: %s\nSet %s: %s with REP:%s" % (self.exercise_name, self.set_num, self.weight_used, self.rpe)


class CardioTraining(Workout):
    def __init__(self, time, workout_name, total_time):
        super().__init__(time, workout_name)
        self.total_time = total_time

    def get_total_time(self):
        return self.total_time

    def set_total_time(self, total_time):
        self.total_time = total_time

    def __str__(self):
        return "CardioTraining Data Structure"


class Running(CardioTraining):
    def __init__(self, time, workout_name, total_time, distance):
        super().__init__(time, workout_name, total_time)
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def __str__(self):
        return "Running Data Structure"


class Cycling(CardioTraining):
    def __init__(self, time, workout_name, total_time, distance):
        super().__init__(time, workout_name, total_time)
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def __str__(self):
        return "Cycling Data Structure"

