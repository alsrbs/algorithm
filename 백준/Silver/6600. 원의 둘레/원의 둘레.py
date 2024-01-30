import math

while True:

    try:
        x1, y1, x2, y2, x3, y3 = map(float, input().split())

        D = 2*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

        center_x = ((x1**2 + y1**2)*(y2 - y3) + (x2**2 + y2**2)*(y3 - y1) + (x3**2 + y3**2)*(y1 - y2))/D
        center_y = ((x1**2 + y1**2)*(x3 - x2) + (x2**2 + y2**2)*(x1 - x3) + (x3**2 + y3**2)*(x2 - x1))/D

        r = ((center_x-x1)**2 + (center_y-y1)**2)**0.5
        C = 2*r*math.pi
        print(round(C, 2))

    except:
        break