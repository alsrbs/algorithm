word = input()
answer = 1
for index in range(1, len(word)):
    if word[index-1] >= word[index]:
        answer += 1

print(answer)
