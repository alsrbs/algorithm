for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    word = input()
    d = {'p': 'q', 'q': 'p', 'b': 'd', 'd': 'b'}
    print(''.join([d[word[i]] for i in range(len(word)-1, -1, -1)]))