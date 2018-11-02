# sinus sorting 
from math import sin

def sorted_sin(s):
    sort_s = sorted(s, key=lambda x : sin(x))
    print(sort_s)

s = eval(input())
sorted_sin(s)
