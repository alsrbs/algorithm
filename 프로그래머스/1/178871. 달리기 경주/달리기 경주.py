
def solution(players, callings):
    d = {b:a for a,b in enumerate(players)}
    for i in callings:
        idx = d[i]
        d[players[idx]] -= 1
        d[players[idx-1]] += 1
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
    return players