def solution(score):
    nums = []
    for i in score:
        nums.append((i[0]+i[1])/2)
    sort_nums = sorted(nums, reverse=True)
    
    d = {}
    for i in range(len(nums)):
        if sort_nums[i] not in d:
            d[sort_nums[i]] = i+1
            
    return [d[i] for i in nums]