for _ in range(10):
    n = int(input())
    print(f'#{n}', end=' ')
    find_word = input()
    word = input()
    print(word.count(find_word))