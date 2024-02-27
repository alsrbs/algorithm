
            
def solution(numbers):
    sorted_nums = sorted(numbers, key=lambda x: str(x)*4, reverse=True)
    result = str(int(''.join(map(str, sorted_nums))))
    return result
