from collections import deque


def bfs(x, y):

    q = deque([(x, y)])
    milo[x][y] = '1'

    while q:
        r, c = q.popleft()

        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
            nr = r + i[0]
            nc = c + i[1]

            if 0<=nr<16 and 0<=nc<16:

                if milo[nr][nc] == '0':  # 이동
                    q.append((nr, nc))
                    milo[nr][nc] = '1'

                elif milo[nr][nc] == '3':  # 도착
                    return 1

    return 0


for t in range(10):

    n = int(input())
    print(f'#{n}', end=' ')
    milo = []

    x, y = 0, 0

    for i in range(16):
        nums = list(input())
        milo.append(nums)

        if '2' in nums:
            x, y = i, nums.index('2')

    print(bfs(x, y))