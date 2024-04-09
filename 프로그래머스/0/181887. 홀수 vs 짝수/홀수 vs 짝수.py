def solution(num_list):
    x, y = 0, 0
    for i in range(len(num_list)):
        if i%2 == 0:
            x += num_list[i]
        else:
            y += num_list[i]
    return max(x, y)