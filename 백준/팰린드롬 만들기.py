from collections import Counter

word = input()
odd_word = ''
even_word = ''
res = Counter(word)
sort_word = sorted(res.keys())
cnt = 0

for i in sort_word:
    if cnt == 2: # 홀수가 2개 이상 등장할 경우
        break
    if res[i] % 2 == 1:
        odd_word = i
        even_word += i * ((res[i]-1) // 2)
        cnt += 1
    else:
        even_word += i*(res[i]//2)

if cnt == 2:
    print("I'm Sorry Hansoo")
else:
    print(even_word + odd_word + even_word[::-1])

