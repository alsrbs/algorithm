def solution(order):
    answer = 0
    keyword = ['iceamericano', 'americanoice', 'hotamericano', 'americanohot', 'americano', 'anything']
    for i in order:
        if i in keyword:
            answer += 4500
        else:
            answer += 5000
    return answer