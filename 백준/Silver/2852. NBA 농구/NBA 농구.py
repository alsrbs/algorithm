n = int(input())
team_score = {'score1': 0, '1_team_cnt': 0, 'score2': 0, '2_team_cnt': 0, 'time_log': 0}
for i in range(n):
    next_log = input().split()
    h, m = next_log[1].split(':')
    time = int(h)*60 + int(m)

    if team_score['1_team_cnt'] > team_score['2_team_cnt']:
        team_score['score1'] += time - team_score['time_log']
    elif team_score['1_team_cnt'] < team_score['2_team_cnt']:
        team_score['score2'] += time - team_score['time_log']

    team_score[str(next_log[0]) + '_team_cnt'] += 1
    team_score['time_log'] = time

    if i == n - 1:
        if team_score['1_team_cnt'] > team_score['2_team_cnt']:
            team_score['score1'] += 48*60 - time
        elif team_score['1_team_cnt'] < team_score['2_team_cnt']:
            team_score['score2'] += 48*60 - time

h1 = '0'*(2-len(str(team_score['score1']//60))) + str(team_score['score1']//60)
m1 = '0'*(2-len(str(team_score['score1']%60))) + str(team_score['score1']%60)
h2 = '0'*(2-len(str(team_score['score2']//60))) + str(team_score['score2']//60)
m2 = '0'*(2-len(str(team_score['score2']%60))) + str(team_score['score2']%60)
print(h1 + ':' + m1)
print(h2 + ':' + m2)