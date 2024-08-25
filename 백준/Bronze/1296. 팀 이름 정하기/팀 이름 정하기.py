yeondu_name = input()
n = int(input())
answer = [-1, 'zzz']
for _ in range(n):
    team_name = input()

    L = yeondu_name.count('L') + team_name.count('L')
    O = yeondu_name.count('O') + team_name.count('O')
    V = yeondu_name.count('V') + team_name.count('V')
    E = yeondu_name.count('E') + team_name.count('E')
    res = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    if answer[0] < res:
        answer[0] = res
        answer[1] = team_name
    elif answer[0] == res:
        answer[1] = min(answer[1], team_name)

print(answer[1])