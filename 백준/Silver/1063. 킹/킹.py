k, s, c = input().split()

move = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
        'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}

k_point = [ord(k[0])-64 - 1, int(k[1]) - 1]
s_point = [ord(s[0])-64 - 1, int(s[1]) - 1]

for _ in range(int(c)):
    word = input()
    n_kw = k_point[0] + move[word][0]
    n_kh = k_point[1] + move[word][1]

    if 0<=n_kw<8 and 0<=n_kh<8:
        if n_kw == s_point[0] and n_kh == s_point[1]:
            n_sw = s_point[0] + move[word][0]
            n_sh = s_point[1] + move[word][1]
            if 0<=n_sw<8 and 0<=n_sh<8:
                k_point[0] += move[word][0]
                k_point[1] += move[word][1]
                s_point[0] += move[word][0]
                s_point[1] += move[word][1]
        else:
            k_point[0] += move[word][0]
            k_point[1] += move[word][1]

print(chr(k_point[0]+65)+ str(k_point[1]+1))
print(chr(s_point[0]+65)+ str(s_point[1]+1))