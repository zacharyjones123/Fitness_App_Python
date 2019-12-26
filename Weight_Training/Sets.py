"""
Set

A set is considered a certain number of reps of an
exercise done in a certain amount of time, followed
by rest
"""


class Sets:

    def __init__(self, num, weight, reps, rest, rpe):
        """
        Init method for Set
        :param: num - number of set
        :param: weight - weight of exercise
        :param: reps - reps of exercises
        :param: rest - rest after exercise
        :param: rpe - 1-10, how hard was it
        :return: nothing
        """
        self.num = num
        self.weight = weight
        self.reps = reps
        self.rest = rest
        self.rpe = rpe

    def get_num(self):
        """
        Getter method for num
        :return: num
        """
        return self.num

    def get_weight(self):
        """
        Getter method for weight
        :return: weight
        """
        return self.weight

    def get_reps(self):
        """
        Getter method for reps
        :return: reps
        """
        return self.reps

    def get_rest(self):
        """
        Getter method for rest
        :return: rest
        """
        return self.rest

    def get_rpe(self):
        """
        Getter method for rpe
        :return: rpe
        """
        return self.rpe

    def set_num(self, num):
        """
        Setter method for num
        :param: num - new num
        :return: nothing
        """
        self.num = num

    def set_weight(self, weight):
        """
        Setter method for weight
        :param: weight - new weight
        :return: nothing
        """
        self.weight = weight

    def set_reps(self, reps):
        """
        Setter method for resp
        :param: reps - new reps
        :return: nothing
        """
        self.reps = reps

    def set_rest(self, rest):
        """
        Setter method for rest
        :param: rest - new rest
        :return: nothing
        """
        self.rest = rest

    def set_rpe(self, rpe):
        """
        Setter method for rpe
        :param: rpe - new rpe
        :return: nothing
        """
        self.rpe = rpe

    def __eq__(self, o) -> bool:
        """
        Equality method
        Sees if 2 sets are exactly alike
        :param: o - another set
        :return: if self and o are the same
        """
        if self.get_num() != o.get_num():
            return False
        elif self.get_weight() != o.get_weight():
            return False
        elif self.get_reps() != o.get_reps():
            return False
        elif self.get_rest() != o.get.rest():
            return False
        elif self.get_rpe() != o.get_rpe():
            return False
        else:
            return True

    def __repr__(self) -> str:
        """
        Repr method for Set
        Ex. Set 1-40lbs-2mins-8RPE
        """
        s = 'Set %s-%slbs-%s reps-%smins-%sRPE' % (self.get_num(), self.get_weight(),
                                                   self.get_reps(), self.get_rest(),
                                                   self.get_rpe())
        return s

    def __str__(self) -> str:
        """
        Str method for Set
        Ex. Set 1-40lbs-2mins-8RPE
        """
        s = 'Set %s-%slbs-%s reps-%smins-%sRPE' % (self.get_num(), self.get_weight(),
                                                   self.get_reps(), self.get_rest(),
                                                   self.get_rpe())
        return s
