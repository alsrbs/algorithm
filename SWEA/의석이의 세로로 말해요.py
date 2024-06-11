for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    words = [input() for _ in range(5)]
    result = ''
    for j in range(15):
        for i in range(5):
            try:
                result += words[i][j]
            except:
                pass
    print(result)