def solution(numlist, n):
    return sorted(sorted(numlist, reverse = True) , key = lambda x : abs(x-n))