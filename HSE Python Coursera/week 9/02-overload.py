from sys import stdin


class Matrix():
    def __init__(self, s):
        self.matrix = []
        self.n_row = len(s)
        self.n_col = 0
        for row in s:
            self.matrix.append(row)
            if len(row) > self.n_col:
                self.n_col = len(row)

    def __str__(self):
        res_str = str()
        first = True
        for row in self.matrix:
            if not first:
                res_str += '\n'
            else:
                first = False
            for elem in row:
                res_str += str(elem) + '\t'
        return res_str

    def size(self):
        return (self.n_row, self.n_col)


# m = Matrix([[1, 0], [0, 1], [0, 1, 12, 11]])
# print(m)
# print(m.size())
exec(stdin.read())
