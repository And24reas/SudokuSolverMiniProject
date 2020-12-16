import wikipedia

s=wikipedia.page("artificial intelligence").content
words = s.split()
#print(words)
no_fors=0
no_tos=0
for word in words:
    if word == "for":
        no_fors+=1
        
    elif word=="to":
        no_tos+=1
print("number of fors")
print(no_fors)
print(no_tos)