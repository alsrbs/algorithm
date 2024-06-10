bin_d = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
         '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

def find():
    for i in range(n):
        for j in range(m - 1, 55, -1):
            if code[i][j] == '1':
                return code[i][j-55:j+1]

for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, m = map(int, input().split())
    code = [input() for _ in range(n)]
    password = find()

    odd, even = 0, 0
    for i in range(0, 50, 7):
        if i%2==0:odd+=bin_d[password[i:i+7]]
        else:even+=bin_d[password[i:i+7]]
    if (odd*3+even)%10==0:print(odd+even)
    else:print(0)
