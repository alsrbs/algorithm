for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    word = input()
    if word == ''.join(list(reversed(word))):
        print(1)
    else:
        print(0)