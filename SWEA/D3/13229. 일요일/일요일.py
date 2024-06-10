for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    day = input()
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7-week.index(day))