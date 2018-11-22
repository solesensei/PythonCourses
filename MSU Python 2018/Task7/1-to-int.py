# decorator converts all float arguments and return value to int
 
def toint(func):
    def wrapper(*args):
        args = tuple(map(lambda x: int(x) if isinstance(x, float) else x, args))
        result_func = func(*args)
        try:
            return int(result_func)
        except:
            return result_func
    return wrapper

@toint
def dou(x):
    return x*2

print(dou((11,22)))
