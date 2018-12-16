# String Divide - Inherit str class, overload // and %

class DivStr(str):
    def __init__(self, s=''):
        self.line = s

    def __floordiv__(self, other):
        other = int(other)
        if other == 0:
            return []
        s = ''
        div_list = []
        block_size = len(self.line) // other
        for i, x in enumerate(self.line):
            if i % block_size == 0 and i != 0:
                div_list.append(s)
                s = ''
            s += x 
        if len(s) == block_size:
            div_list.append(s)
        return div_list
        
    def __mod__(self, other):
        other = int(other)
        if other == 0:
            return None
        last_part_size = len(self.line) % other
        return self.line[-last_part_size:] if last_part_size != 0 else ''  

    def __str__(self):
        return self.line

# a = DivStr("XcDfQWEasdEldasldlsaldlasdlalsdRTdfg")
# print(a//4)
# print(a%4)