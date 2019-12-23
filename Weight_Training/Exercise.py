"""
Exercise

An Exercise is considered a movement, with a name,
and done for a certain number of sets
"""


class Exercise:

    def __init__(self, name, sets):
        """
        Init method for Exercise
        :param: name - name of the exercise
        :param: sets - array of Set objects
        """
        self.name = name
        self.sets = sets

    def get_name(self):
        """
        Getter method for name
        :return: name
        """
        return self.name

    def get_sets(self):
        """
        Getter method for sets
        :return: sets
        """
        return self.sets

    def set_name(self, name):
        """
        Setter method for name
        :param: name - new name
        :return: nothing
        """
        self.name = name

    def set_sets(self, sets):
        """
        Setter method for sets
        :param: sets - new array of sets
        :return: nothing
        """
        self.sets = sets

    def __eq__(self, o) -> bool:
        """
        Equality method for Exercise
        See if 2 exercises are the same
        :param: o - other exercise
        :return: if the 2 exercises are the same
        """
        if self.get_name() != o.get_name():
            return False
        elif self.get_sets() != o.get_sets():
            return False
        else:
            return True

    def __repr__(self) -> str:
        """
        Repr method for Exercise
        Give Repr representation for Exercise
        """
        s = "Exercise %s" % (self.get_name())
        for s in self.get_sets():
            s += "\n%s" % s
        return s

    def __str__(self):
        """
        Str method for Exercise
        Give Str representation for Exercise
        """
        s = "Exercise %s" % (self.get_name())
        for l in self.get_sets():
            s += "\n%s" % l
        return s
