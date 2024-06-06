for i in range(1, int(input())+1):
    word = input()
    for j in range(1, 11):
        if word[:j] == word[j:j*2]:
            print(f'#{i} {j}')
            break