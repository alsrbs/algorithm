for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')

    word = input()

    ans = 'NO'
    if word == word[::-1]:
        front_word = word[:(len(word)-1)//2]
        back_word = word[(len(word) - (len(word)-1)//2):]
        if front_word == front_word[::-1] and back_word == back_word[::-1]:
            ans = 'YES'

    print(ans)