# Custom Dots Class (StrangeDots)

class Dots:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sequence(self, block):
        self.step = (self.b - self.a) / (int(block) - 1)
        return [self.a + i*self.step for i in range(int(block))]

    def get_element(self, idx, block):
        seq = self.get_sequence(block)
        if idx < 0:
            seq = [self.a + i*self.step for i in range(idx, 0)] + seq
        if idx >= block:
            seq = seq + [self.a + i*self.step for i in range(block, idx+1)]
        return seq[idx] if idx > 0 else seq[0]

    def get_range(self, start, end, step):
        self.get_sequence(step)
        start = 0 if not start else start
        end = step if not end else end
        return [self.get_element(x, step) for x in range(start, end)]

    def __getitem__(self, op):
        if isinstance(op, slice) and op.step:
            return self.get_range(op.start, op.stop, op.step)
        elif isinstance(op, slice) and not op.step:
            return self.get_element(op.start, op.stop)
        else:
            return self.get_sequence(op)
           

a = Dots(-1,1)
print('*a[5]', *a[5])
print('a[0:5]', a[0:5])
print('a[2:5]', a[2:5])
print('a[4:5]', a[4:5])
print('a[7:5]', a[7:5])
print('a[-7:5]', a[-7:5])
print('*a[1:3:5]', *a[1:3:5])
print('*a[:3:5]', *a[:3:5])
print('*a[2::5]', *a[2::5])
print('*a[::5]', *a[::5])
print('*a[-2:6:5]', *a[-2:6:5])