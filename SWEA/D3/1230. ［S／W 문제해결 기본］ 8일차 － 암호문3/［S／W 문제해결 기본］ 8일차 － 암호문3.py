for t in range(1, 11):
    print(f'#{t}', end=' ')
    n = int(input())
    password = list(input().split())
    m = int(input())
    cmd = list(input().split())
    for i in range(len(cmd)):
        if cmd[i] == 'I':
            for j in range(int(cmd[i+2])):
                password.insert(int(cmd[i+1])+j, int(cmd[i+3+j]))
        elif cmd[i] == 'D':
            del password[int(cmd[i+1]):int(cmd[i+1])+int(cmd[i+2])]
        elif cmd[i] == 'A':
            password+=cmd[i+2:i+2+int(cmd[i+1])]
    print(*password[:10])