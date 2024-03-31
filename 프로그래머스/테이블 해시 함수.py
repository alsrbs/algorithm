data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3

data = sorted(data, key = lambda x : (x[col-1], -x[0]))

answer = 0
for i in range(row_begin-1, row_end):
    s_i = sum([x % (i + 1) for x in data[i]])
    answer += s_i
print(answer)