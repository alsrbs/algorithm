abc = 'abcdefghijklmnopqrstuvwxyz'
for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    word = input()
    result = 0
    for i in range(min(27, len(word))):
        if abc[i]==word[i]:result+=1
        else:break
    print(result)