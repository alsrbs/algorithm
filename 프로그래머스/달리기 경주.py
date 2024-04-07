players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

d = {b:a for a,b in enumerate(players)}
for i in callings:
    idx = d[i]
    d[players[idx]] -= 1
    d[players[idx-1]] += 1
    players[idx], players[idx - 1] = players[idx - 1], players[idx]
print(players)