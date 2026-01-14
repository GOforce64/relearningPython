class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = self.matrix_string.split("\n")

    def row(self, index):
        row = self.rows[index - 1].split()
        return list(map(int, row))

    def column(self, index):
        column = []
        for row in self.rows:
            row = row.split()
            column.append(row[index - 1])
        return list(map(int, column))
