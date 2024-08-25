yeondu_name = input()
n = int(input())

name_list = []
for i in range(n):
    name_list.append(input())

name_list = sorted(set(name_list))

answer = [-1, 'zzz']
for team_name in name_list:

    L = yeondu_name.count('L') + team_name.count('L')
    O = yeondu_name.count('O') + team_name.count('O')
    V = yeondu_name.count('V') + team_name.count('V')
    E = yeondu_name.count('E') + team_name.count('E')
    res = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    if answer[0] < res:
        answer[0] = res
        answer[1] = team_name

print(answer[1])