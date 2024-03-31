def solution(numbers):
    numbers.sort()
    max_num = [numbers[0]*numbers[1], numbers[-1]*numbers[-2]]
    return max(max_num)