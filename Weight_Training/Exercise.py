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

    def __eq__(self, o) -> bool:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self):
        s = '----------'
        s += '%s\n' % self.name
        s += '----------'
        return s