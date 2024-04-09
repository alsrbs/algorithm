def solution(a, b, c, d):
    nums = sorted([a, b, c, d])
    
    if len(set(nums)) == 1:
        return a*1111
    
    if len(set(nums)) == 2:
        
        if nums.count(nums[0]) == 3:
            return (nums[0]*10+nums[-1])**2
        
        if nums.count(nums[0]) == 1:
            return (nums[-1]*10+nums[0])**2
        
        return (nums[0]+nums[-1])*abs(nums[0]-nums[-1])
    
    if len(set(nums)) == 3:
        if nums.count(nums[0]) == 2:
            return nums[2]*nums[3]
        elif nums.count(nums[1]) == 2:
            return nums[0]*nums[3]
        elif nums.count(nums[2]) == 2:
            return nums[0]*nums[1]
    
    return min(nums)