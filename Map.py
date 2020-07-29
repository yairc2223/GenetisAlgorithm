class Map:

    def __init__(self, cells_list, fitness):
        self.formation = cells_list
        self.fitness_score = fitness

    # formulate string representation of the map
    def to_string(self):
        str_form = ""
        for cell in self.formation:
            str_form += str(cell.color)
        return str_form

    def set_fit(self, n):
        self.fitness_score = n
