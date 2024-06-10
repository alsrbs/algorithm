for t in range(1, 11):
    print(f'#{t}', end=' ')
    n, password = input().split()
    for i in range(int(n)//2):
        password = password.replace('99', '').replace('11', '').replace('22', '').replace('33', '').replace('44', '').replace('55', '').replace('66', '').replace('77', '').replace('88', '').replace('00', '')
    print(int(password))