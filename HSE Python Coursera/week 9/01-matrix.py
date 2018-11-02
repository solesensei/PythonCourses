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
        res_str = str('')
        size = self.size()[0]*self.size()[1]
        for i, row in enumerate(self.matrix):
            if i != 0:
                res_str += '\n'
            for j, elem in enumerate(row):
                res_str += str(elem)
                if i*self.n_col+j != size-1:
                    res_str += '\t'
                print(i*self.n_col+j)
        return res_str

    def size(self):
        return (self.n_row, self.n_col)


# m = Matrix([[1, 0], [0, 1], [0, 1, 12, 11]])
# print(m)
# print(m.size())
m = Matrix([[1, 1, 1], [0, 100, 10]])
print(str(m))
print(str(m) == '1\t1\t1\n0\t100\t10')
# exec(stdin.read())
