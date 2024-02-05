import sys

input = sys.stdin.readline


def are_similar_words(word1, word2):
    cnt = 0

    for i in word2:
        if i in word1:
            word1.remove(i)
        else:
            cnt += 1


    if cnt < 2 and len(word1) < 2:
        return True

N = int(input())
target = input()

result = 0
for i in range(N - 1):
    word = input()
    if abs(len(target) - len(word)) > 1:continue
    if are_similar_words(list(target), word):
        result += 1

print(result)
