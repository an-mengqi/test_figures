class Figure:
    def __init__(self):
        self.name = None
        self.area = None
        self.perimeter = None

    def add_area(self, figure):
        if isinstance(figure, Figure) is True:
            return self.area + figure.area
        else:
            raise ValueError('Wrong value given to add_area(), not a figure!')
