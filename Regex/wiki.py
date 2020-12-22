import wikipedia

s=wikipedia.page("artificial intelligence").content
words = s.split()
#print(words)
no_fors=0
no_tos=0
for word in words:
    print(word)
print("number of fors")
print(no_fors)
print(no_tos)