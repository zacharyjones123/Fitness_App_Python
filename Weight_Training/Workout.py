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

    def __eq__(self, o) -> bool:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        s = ''
        s += "Workout - %s\n" % self.date
        s += "To come\n"
        return s
