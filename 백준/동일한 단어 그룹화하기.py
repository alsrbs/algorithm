list_word = []
for i in range(int(input())):
    word = input()
    w =''.join(sorted(word))
    list_word.append(w)
print(len(set(list_word)))