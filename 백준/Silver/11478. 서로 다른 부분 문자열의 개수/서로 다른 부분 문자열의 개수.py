word=input()
total=set()
for i in range(len(word)):
    for j in range(i,len(word)):
        total.add(word[i:j+1])
print(len(total))