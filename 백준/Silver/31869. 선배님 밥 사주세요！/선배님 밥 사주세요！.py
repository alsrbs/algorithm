n = int(input())

log = {}
for _ in range(n):
    name, w, d, p = input().split()
    log[name] = [(int(w)-1)*7 + int(d), int(p)]   # (주를 일 단위로 변환 + 일, 비용)

data = [0]*7*10  # 10주 * 7일 = 70일
for _ in range(n):
    name, p = input().split()
    if int(p) - log[name][1] >= 0:  # 충분한 돈이 있다면
        data[log[name][0]] = 1  # 해당 날짜를 1로 설정

max_count = 0  # 연속된 1의 최대 개수
current_count = 0  # 현재 연속된 1의 개수
for value in data:
    if value == 1:
        current_count += 1  #
    else:
        max_count = max(max_count, current_count)  # 연속이 끝나면 최대값을 갱신
        current_count = 0  # 현재 카운트를 초기화

max_count = max(max_count, current_count)

print(max_count)