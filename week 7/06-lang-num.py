n = int(input())
all_lang = set()
one_lang = set()
for i in range(n):
    m = int(input())
    lang = set()
    for j in range(m):
        lang.add(input())
    all_lang |= lang
    if i == 0:
        one_lang = all_lang.copy()
    one_lang &= lang
print(len(one_lang))
for lang in one_lang:
    print(lang)
print(len(all_lang))
for lang in all_lang:
    print(lang)
