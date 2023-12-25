dic_num = {
    '0': '####.##.##.####',
    '1': '..#..#..#..#..#',
    '2': '###..#####..###',
    '3': '###..####..####',
    '4': '#.##.####..#..#',
    '5': '####..###..####',
    '6': '####..####.####',
    '7': '###..#..#..#..#',
    '8': '####.#####.####',
    '9': '####.####..####'
}

def match_rate(st):
    num = []
    for i in range(10):
        c = True
        for j in range(15):
            if st[j] != dic_num[str(i)][j] and st[j] == '#':
                c = False
                break
        if c:
            num += [i]
    return str(min(num))

nums = [list(input().split()) for _ in range(5)]
res = ''
for j in range(4):
    num_st = ''
    for i in range(5):
        num_st += nums[i][j]
    res += match_rate(num_st)
print(res[0]+res[1]+':'+res[2]+res[3])