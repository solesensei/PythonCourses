# Letter Attribute - any attribute custom class

class LetterAttr(object):

    attr = {}

    def __setattr__(self, name, value):
        if name not in LetterAttr.attr.keys():
            LetterAttr.attr[name] = name
        if name != value:
            old_value = LetterAttr.attr[name]
            cur_value = list(value)
            for x in value:
                if x not in old_value and x in cur_value:
                    cur_value.remove(x)
            res = ''
            for x in cur_value:
                res += x
            LetterAttr.attr[name] = res
        return LetterAttr.attr[name]

    def __getattr__(self, name):
        if name in LetterAttr.attr.keys():
            return LetterAttr.attr[name]
        return self.__setattr__(name, name)

A = LetterAttr()
print(A.letter)
print(A.digit)
A.letter = "teller"
print(A.letter)
A.letter = "fortune teller"
print(A.letter)

A = LetterAttr()
print(A.Q, A.___)
A.Q="QqQq"
print(A.Q)
A.Base="END"
print("<{}>".format(A.Base))