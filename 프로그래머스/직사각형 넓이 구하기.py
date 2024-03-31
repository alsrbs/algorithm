dots = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
w = []
l = []

for i in dots:
    w.append(i[0])
    l.append(i[1])

print(abs(max(w)-min(w))*abs(max(l)-min(l)))