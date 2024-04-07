def solution(n, slicer, num_list):
    answer = {1: num_list[:slicer[1]+1], 2: num_list[slicer[0]:], 3: num_list[slicer[0]:slicer[1]+1], 4: num_list[slicer[0]:slicer[1]+1:slicer[2]]}
    return answer[n]