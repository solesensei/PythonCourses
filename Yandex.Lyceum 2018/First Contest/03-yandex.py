text = input()

symbols = {}

for i in range(len(text)):
    char = text[i]
    if char in symbols:
        value = symbols.pop(char)
        symbols[char] = value + 1
    else:
        symbols[char] = 1

all_symbols = len(text)
for key in sorted(symbols.keys()):
    the_symbol = symbols.pop(key)
    procent = the_symbol / all_symbols * 100
    print(key, '{:.2f}'.format(procent))
