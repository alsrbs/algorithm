def solution(emergency):
    nums = sorted(emergency, reverse=True)
    return [nums.index(i) + 1 for i in emergency]