def find():
    for j in range(100, -1, -1):
        for k in range(100 - (j-1)):
            for i in range(100):
                word1 = arr[i][k:k+j]
                word2 = ''.join(arr_r[i][k:k + j])
                if word1 == word1[::-1] or word2 == word2[::-1]:
                    return j

for _ in range(1, 11):
    n = int(input())
    print(f'#{n}', end=' ')
    arr = [input() for _ in range(100)]
    arr_r = list(zip(*arr))
    print(find())
