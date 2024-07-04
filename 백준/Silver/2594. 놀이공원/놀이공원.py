n = int(input())
time_log = [(1320, 1320)]
for i in range(n):
    s, e = input().split()
    s_time = int(s[:2])*60 + int(s[2:]) - 10
    e_time = int(e[:2]) * 60 + int(e[2:]) + 10
    time_log.append((s_time, e_time))

time_log.sort()

max_time = 0
last = 600
for i in range(n+1):
    max_time = max(max_time, time_log[i][0] - last)
    last = max(last, time_log[i][1])

print(max_time)