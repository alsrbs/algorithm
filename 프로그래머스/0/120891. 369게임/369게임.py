def solution(order):
    order = str(order)
    return order.count('9') + order.count('6') + order.count('3')