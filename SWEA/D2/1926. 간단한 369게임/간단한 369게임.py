n = int(input())
for i in range(1, n+1):
    i = str(i)
    if '3' in i or '6' in i or '9' in i:
        print('-' * (list(i).count('3') + list(i).count('6') + list(i).count('9')), end=' ')
    else:
        print(i, end=' ')