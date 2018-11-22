# Reverse Polish Notation RPN (postfix)


def check_int(x):
    if x[0] == '-':
        return x[1:].isdigit()
    return x.isdigit()

words = input().split()
clean_list = [] 
ops = ('+', '-', '*')
for word in words:
    if check_int(word) or word in ops:
        clean_list.append(word)

stack = [0]
for elem in clean_list:
    if elem in ops:
        a, b = stack.pop(), stack.pop()
        stack.append(eval(f"{b} {elem} {a}"))
    else:
        stack.append(int(elem))

print(stack.pop())
