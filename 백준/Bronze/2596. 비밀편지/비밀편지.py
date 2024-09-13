n = int(input())
str = input()
dic = {
    '000000': 'A',
    '001111': 'B',
    '010011': 'C',
    '011100': 'D',
    '100110': 'E',
    '101001': 'F',
    '110101': 'G',
    '111010': 'H'
}

answer = ''

for i in range(0, len(str), 6):
    s = str[i:i+6]
    if s in dic:
        answer += dic[s]
    else:
        c = set()
        for k in dic:
            cnt = 0
            for j in range(6):
                if k[j] != s[j]:
                    cnt += 1
                if cnt >= 2:
                    break
            else:
                if cnt == 1:
                    answer += dic[k]
                c.add(cnt)
        if 1 not in c:
            answer = len(answer) + 1

    if type(answer) == type(1):
        break

print(answer)
