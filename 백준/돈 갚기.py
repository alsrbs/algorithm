def month(r, b, m):
    count = 0

    while True:
        count += 1
        x = round((b*100)*(r/100), 0)   # 이자를 센트로 변환
        b = round(((b*100) + x)/100, 2) # 원금을 센트로 변환 후 이자를 더하고 달러로 변환
        b -= m

        if b <= 0:
            print(count)
            return

        if count >= 1200:
            print('impossible')
            return


for _ in range(int(input())):
    R, B, M = map(float, input().split())
    month(R, B, M)
