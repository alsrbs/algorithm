t = int(input())
for i in range(t):
    answer = 0
    nums = list(map(int, input().split()))
    for num in nums:
        if num%2 != 0:
            answer += num

    print(f'#{i} {answer}')