import sys
N, M = map(int, input().split())
words = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip() 
    if len(word) < M: continue
    if word not in words:
        words[word] = [len(word), 1]
    else:
        words[word][1] += 1
sorted_words = sorted(words.items(), key=lambda x: (-x[1][1], -x[1][0], x[0]))
for i in sorted_words:
    print(i[0])