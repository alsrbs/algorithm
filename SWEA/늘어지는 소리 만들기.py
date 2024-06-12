for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    word = list(input())
    h = int(input())
    idx = sorted(map(int, input().split()), reverse=True)
    for i in idx:
        word.insert(i, '-')
    print(''.join(word))