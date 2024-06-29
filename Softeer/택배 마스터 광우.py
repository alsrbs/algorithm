from itertools import permutations

# 레일 개수, 바구니 무게, 횟수
n, m, k = map(int, input().split())
rail = sorted(map(int, input().split()))

perm = permutations(rail, n)

ans = 1e9
for i in perm:
    now_rails = i

    idx = 0
    bucket = 0
    work = k
    cnt = 0

    while work:

        if bucket + now_rails[idx%n] <= m:
            bucket += now_rails[idx%n]
            idx += 1
        else:
            cnt += bucket
            bucket = 0
            work -= 1

    ans = min(ans, cnt)

print(ans)

