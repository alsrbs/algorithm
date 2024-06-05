t = int(input())
for i in range(t):
    day = input()
    if int(day[4:6]) in [1, 3, 5, 7, 8, 10, 12] and 1<=int(day[6:])<=31:
        print(f'#{i+1} {day[:4]}/{day[4:6]}/{day[6:]}')
    elif int(day[4:6]) in [4, 6, 9, 11] and 1<=int(day[6:])<=30:
        print(f'#{i + 1} {day[:4]}/{day[4:6]}/{day[6:]}')
    elif int(day[4:6]) == 2 and 1<=int(day[6:])<=28:
        print(f'#{i + 1} {day[:4]}/{day[4:6]}/{day[6:]}')
    else:
        print(f'#{i+1} {-1}')