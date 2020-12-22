import wikipedia
import re

s=wikipedia.page("artificial intelligence").content
words = s.split()
#print(words)
no_fors=0
no_tos=0
pattern = '[as]'
pattern2 = '[0-9]'
words_a = []
words_s = []
numbers = []
for word in words:
    if re.match(pattern, word):
        if word[0]=='a':
            words_a.append(word)
        else:
            words_s.append(word)
for word in words:
    if re.match(pattern2, word):
        numbers.append(word)

print(set(words_a))
print()
print()
print(set(words_s))
print()
print()
print(numbers)

    