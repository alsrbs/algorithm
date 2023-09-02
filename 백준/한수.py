def is_hansu(n):
    # 숫자를 문자열로 변환하여 자릿수를 확인합니다.
    digits = str(n)
    n_digits = len(digits)

    # 한자리 숫자나 두자리 숫자는 모두 한수입니다.
    if n_digits <= 2:
        return True

    # 각 자릿수 간의 차이를 계산합니다.
    common_difference = int(digits[1]) - int(digits[0])

    # 자릿수를 순회하면서 등차수열인지 확인합니다.
    for i in range(2, n_digits):
        if int(digits[i]) - int(digits[i - 1]) != common_difference:
            return False
    return True

def count_hansu(N):
    count = 0
    for num in range(1, N + 1):
        if is_hansu(num):
            count += 1
    return count

N = int(input())

# 한수의 개수를 계산하고 출력합니다.
print(count_hansu(N))
