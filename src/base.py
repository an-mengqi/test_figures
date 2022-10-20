class Figure:
    @property
    def area(self):
        return 0

    def add_area(self, figure):
        if isinstance(figure, Figure) is True:
            return self.area + figure.area
        else:
            raise ValueError('Wrong value given to add_area(), not a figure!')
