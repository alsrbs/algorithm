n, w, l = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [0]*w
ans = 0
s = 0
while bridge:
    ans += 1
    s -= bridge.pop(0)
    if truck:
        if s + truck[0] <= l:
            x = truck.pop(0)
            s += x
            bridge.append(x)
        else:
            bridge.append(0)

print(ans)