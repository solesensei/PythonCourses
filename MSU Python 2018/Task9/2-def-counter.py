# Def Counter - Inherit collections.Counter class, with missing values changed 0 -> missing

import collections

class DefCounter(collections.Counter):
    def __init__(self, *args, **kwargs):
        self.m = -1
        if 'missing' in kwargs.keys():
            self.m = kwargs['missing']
            kwargs.pop('missing', None) 
        super().__init__(*args, **kwargs)

    def __missing__(self, key):
        return self.m

A = DefCounter("QWEqweQWEqweQWE", missing=-10)
print(A)
print(A["Z"])
A["P"]+=5
print(A)
A = DefCounter(a=2,b=3,c=8,missing=2)
print(A["a"], A["c"], A["f"])
