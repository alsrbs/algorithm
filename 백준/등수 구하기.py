N, new_point, P = map(int, input().split())
point_list = []
if N > 0 :
    point_list += list(map(int, input().split()))
point_list.append(new_point)
point_list.sort(reverse=True)
if new_point in point_list[P:]:print(-1)
else:
    d = {}
    for i in range(len(point_list[:P])):
        d[point_list[:P][i]] = i+1
    print(d[new_point] - point_list[:P].count(new_point)+1)
