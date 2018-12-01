
# Counting class instance
 
class we:
    count = 0 
    def __init__(self):
        we.count += 1

    def __del__(self):
        we.count = we.count - 1 if we.count > 0 else 0

a = we()
print(a.count)
b, c = we(), we(),
print(a.count, b.count, c.count)
del b
print(a.count)
