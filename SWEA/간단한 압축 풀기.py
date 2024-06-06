for t in range(1, int(input())+1):
    print(f'#{t}')
    n = int(input())
    word = ''
    for i in range(n):
        w, num = input().split()
        word += w*int(num)

    for i in range(len(word) // 10 + 1):
        print(word[:10])
        word = word[10:]