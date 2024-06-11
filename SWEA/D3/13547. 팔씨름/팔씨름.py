for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    score = input()
    print('NO' if 15 - len(score) + score.count('o') < 8 else 'YES')
