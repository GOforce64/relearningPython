PLANT_DICT = {"G" : "Grass",
              "C" : "Clover",
              "R" : "Radishes",
              "V" : "Violets"}

class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
                                            "Ileana","Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram
        self.students = students

    def plants(self, student):
        plants = []
        rows = self.diagram.split("\n")
        sorted_names = sorted(self.students)
        for possition, name in enumerate(sorted_names):
            if name == student:
                possition = possition * 2
                plants.append(PLANT_DICT[rows[0][possition]])
                plants.append(PLANT_DICT[rows[0][possition + 1]])
                plants.append(PLANT_DICT[rows[1][possition]])
                plants.append(PLANT_DICT[rows[1][possition + 1]])
                break
        return plants
        
