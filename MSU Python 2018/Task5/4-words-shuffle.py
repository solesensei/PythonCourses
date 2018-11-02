# Check shuffle of words coincidence

s1 = input().upper()
s2 = input().upper()

words_input = ''.join((char if char.isalnum() else ' ') for char in s1).split()
words_shuffle = ''.join((char if char.isalnum() else ' ') for char in s2).split()

for word in words_input:
    if word in words_shuffle:
        words_shuffle.remove(word)
    else:
        words_shuffle.append('False')
        break

print(('False' if len(words_shuffle) else 'True'))