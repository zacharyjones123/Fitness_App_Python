"""
Workout

A Workout is considered to have a date and consists
of exercises
"""


class Workout:

    def __init__(self, date, exercises):
        """
        Init method for Workout
        :param: date - date of the workout
        :param: exercises - array of Exercise objects
        """
        self.date = date
        self.exercises = exercises

    def get_date(self):
        """
        Getter method for date
        :return: date
        """
        return self.date

    def get_exercises(self):
        """
        Getter method for exercises
        :return: exercises
        """
        return self.exercises

    def set_date(self, date):
        """
        Setter method for date
        :param: date
        :return: nothing
        """
        self.date = date

    def set_exercises(self, exercises):
        """
        Setter method for exercises
        :param: exercises
        :return: nothing
        """
        self.exercises = exercises

    def add_exercise(self, exercise):
        """
        Add exercise to array of exercises
        :param: exercise to add
        :return: nothing
        """
        self.exercises.append(exercise)

    def __eq__(self, o) -> bool:
        """
        Eauality method for Workout
        :param: o - other Workout
        :return: True if equal, False if not equal
        """
        if self.get_name() != o.get_name():
            return False
        elif self.get_exercises() != o.get_exercises():
            return False
        else:
            return True

    def __repr__(self) -> str:
        """
        Repr method for Workout
        :return: repr for Workout
        """
        s = 'Date: %s' % self.date
        for p in self.get_exercises():
            s += '\n%s' % p
        return s

    def __str__(self) -> str:
        """
        Str method for Workout
        :return: str for Workout
        """
        s = 'Date: %s' % self.date
        for p in self.get_exercises():
            s += '\n%s' % p
        return s
