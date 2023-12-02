bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]

attacks.sort(key=lambda x:-x[0])
max_health = health
t = 0
c = bandage[0]
hell = bandage[1]
plus_hell = bandage[2]

while attacks:
    t += 1
    print(health)
    if attacks[-1][0] == t:
        attack = attacks.pop()
        health -= attack[1]
        c = bandage[0]
        if health <= 0:
            health = -1
            break
    else:
        health += hell
        c -= 1
        if c == 0:
            health += plus_hell
            c = bandage[0]
        if health >= max_health:
            health = max_health

print(health)

