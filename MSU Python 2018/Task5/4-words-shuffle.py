# Check shuffle of words coincidence


s1 = input().upper()
s2 = input().upper()

words_input = [word if word[-1].isalnum() else word[:-1] for word in s1.split()]
words_shuffle = [word if word[-1].isalnum() else word[:-1] for word in s2.split()]
words_input += [word[-1] if not word[-1].isalnum() else '' for word in s1.split()] 
words_shuffle += [word[-1] if not word[-1].isalnum() else '' for word in s2.split()]

if sorted(words_input) == sorted(words_shuffle):
    print('True')
else:
    print('False')
