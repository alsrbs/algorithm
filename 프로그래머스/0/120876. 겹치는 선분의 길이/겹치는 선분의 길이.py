def solution(lines):
    nums = [0]*201
    for i in lines:
        for j in range(i[0]+100, i[1]+100):
            nums[j] += 1
    return nums.count(2) + nums.count(3)