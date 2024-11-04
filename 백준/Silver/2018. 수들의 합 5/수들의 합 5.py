n = int(input())

answer = 0
for k in range(1, n + 1):
    if k * (k - 1) // 2 >= n:
        break

    # a가 자연수인지 확인
    if (n - (k * (k - 1)) // 2) % k == 0:
        a = (n - (k * (k - 1)) // 2) // k
        if a > 0:
            answer += 1

print(answer)
