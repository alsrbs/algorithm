def solution(q, r, code):
    return ''.join(code[idx] for idx in range(len(code)) if idx%q == r)