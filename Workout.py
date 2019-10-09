class Workout:

    def __init__(self, date, exercises):
        self.date = date
        self.exercises = exercises

    def get_date(self):
        return self.date

    def get_exercises(self):
        return self.exercises

    def set_date(self, date):
        self.date = date

    def set_exercises(self, exercises):
        self.exercises = exercises

    def __str__(self):
        s = ''
        s += "Workout - %s\n" % self.date
        s += "To come\n"
        return s


class Exercise:

    def __init__(self, name, sets):
        self.name = name
        self.sets = sets

    def get_name(self):
        return self.name

    def get_sets(self):
        return self.sets

    def set_name(self, name):
        self.name = name

    def set_sets(self, sets):
        self.sets = sets

    def __str__(self):
        s = '----------'
        s += '%s\n' % self.name
        s += '----------'
        return s


class Set:

    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight
