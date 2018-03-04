x = float(input())
fraction = x - int(x)

if fraction < 0.5:
    x = int(x)
else:
    x = int(x+1)
print(x)
