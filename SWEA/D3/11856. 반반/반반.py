for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    print('Yes' if len(set(list(input())))==2 else 'No')