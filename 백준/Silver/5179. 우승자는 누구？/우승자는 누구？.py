K = int(input())
for test in range(K):
    print(f'Data Set {test + 1}:')

    M, N, P = map(int, input().split())

    # 각 참가자의 제출 기록을 저장
    log = {}

    for _ in range(N):
        p, m, t, j = input().split()
        p = int(p)
        t = int(t)
        j = int(j)
        m_index = ord(m) - 65  # 문제 번호를 인덱스로 변환 (A=0, B=1, ...)

        if p not in log:
            log[p] = [[0] * M, [False] * M, 0]  # 문제 점수, 문제 정답 여부, 푼 문제 수

        # 문제를 맞힌 경우
        if j == 1 and not log[p][1][m_index]:
            log[p][1][m_index] = True  # 문제 정답 여부 갱신
            log[p][2] += 1
            log[p][0][m_index] += t

        # 문제를 틀린 경우
        elif j == 0 and not log[p][1][m_index]:
            log[p][0][m_index] += 20


    total_log = {}
    for k, v in log.items():
        total_time = 0
        for i in range(M):
            if v[1][i]:
                total_time += v[0][i]

        total_log[k] = (v[2], total_time)

    # 푼 문제 수는 내림차순, 총점은 오름차순
    ans = sorted(total_log.items(), key=lambda x:(-x[1][0], x[1][1]))

    for i in ans:
        print(i[0], i[1][0], i[1][1])

    print()