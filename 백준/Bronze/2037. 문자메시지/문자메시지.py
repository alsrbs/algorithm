p, w = map(int, input().split())
word = input()
nums = [
    {'A', 'B', 'C'},
    {'D', 'E', 'F'},
    {'G', 'H', 'I'},
    {'J', 'K', 'L'},
    {'M', 'N', 'O'},
    {'P', 'Q', 'R', 'S'},
    {'T', 'U', 'V'},
    {'W', 'X', 'Y', 'Z'}
    ]

answer = 0
for i in range(len(word)):
    if word[i] in {' ', 'A', 'D', 'G', 'J', 'M', 'P', 'T', 'W'}:
        answer += p
    elif word[i] in {'B', 'E', 'H', 'K', 'N', 'Q', 'U', 'X'}:
        answer += p*2
    elif word[i] in {'S', 'Z'}:
        answer += p*4
    else:
        answer += p*3

    if i > 0:
        for num in nums:
            if word[i-1] in num and word[i] in num:
                answer += w
                break

print(answer)