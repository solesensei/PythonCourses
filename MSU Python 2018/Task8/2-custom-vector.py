# Class Vector (custom)

class vector:
    def __init__(self, args=[]):
        self.vec = []
        for arg in args:
            self.vec.append(arg)
    
    def __add__(self, other):
        if isinstance(other, range):
            other = list(other)
        if isinstance(other, self.__class__):
            diff = len(self.vec) - len(other.vec)
            if diff > 0:
                other.vec += [0 for i in range(diff)]
            else:
                self.vec += [0 for i in range(-diff)]
            return vector([a + b for a, b in zip(self.vec, other.vec)])
        elif isinstance(other, int):
            return vector([x + other for x in self.vec])
        elif isinstance(other, list):
            diff = len(self.vec) - len(other)
            if diff > 0:
                other += [0 for i in range(diff)]
            else:
                self.vec += [0 for i in range(-diff)]
            return vector([a + b for a, b in zip(self.vec, other)])
        else:
            raise TypeError(f'Unsupported + operand {type(other)}')
    
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __neg__(self):
        return vector([-x for x in self.vec])

    def __sub__(self, other):
        if isinstance(other, list):
             return self.__add__([-x for x in other])
        return self.__add__(-other)    

    def __getitem__(self, pos):
        return self.vec[pos]
    
    def __str__(self):
        tmp = str()
        for x in self.vec:
            tmp += str(x) + ':'
        return tmp[:-1]

    def push(self, elem):
        self.vec.append(elem)

    def pop(self):
        return self.vec.pop()

# a, b = vector([2,1,2,1,2,1,2,1]), vector(range(8))
# print(a, b, a+b, b+range(8), range(8)+b)