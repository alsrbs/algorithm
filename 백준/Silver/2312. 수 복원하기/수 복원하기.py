def eratosthenes(num):
    MAX = num + 1
    LIM = int(num ** 0.5) + 1
    RSET = lambda start, end, gap: set(range(start, end, gap))

    # 5 (mod 6) 과 1 (mod 6)을 참으로 설정한다. 이들은 2의배수도 아니고 3의 배수도 아닌 숫자집합이다.
    # 단, 1은 소수가 아니기에 1 (mod 6)은 7부터 시작한다.
    prime = RSET(5, MAX, 6) | RSET(7, MAX, 6)
    if num > 2: prime.add(3)  # 3 추가
    if num > 1: prime.add(2)  # 2 추가
    for i in range(5, LIM, 6):
        # 5 (mod 6) 부분
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
        # 1 (mod 6) 부분
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)

    return sorted(prime)

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

decimal = eratosthenes(max(nums))

for num in nums:
    d = {}
    for i in decimal:
        if num == 0:
            break
        if num % i == 0:
            c = 0
            while True:
                if num % i != 0:
                    break
                c += 1
                num = num//i
            d[i] = c
    for i in sorted(d.items(), key=lambda x: x[0]):
        print(*i)
