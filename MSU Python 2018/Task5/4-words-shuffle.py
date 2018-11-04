# Check shuffle of words coincidence


s1 = input().upper()
s2 = input().upper()

words_input = [word if word[-1].isalnum() else word[:-1] for word in s1.split()]
words_shuffle = [word if word[-1].isalnum() else word[:-1] for word in s2.split()]
words_input += [word[-1] if not word[-1].isalnum() else '' for word in s1.split()] 
words_shuffle += [word[-1] if not word[-1].isalnum() else '' for word in s2.split()]

for word in words_input:
    if word in words_shuffle:
        words_shuffle.remove(word)
    else:
        words_shuffle.append('False')
        break

print(('False' if len(words_shuffle) else 'True'))
