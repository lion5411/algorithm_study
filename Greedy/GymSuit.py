def solution(n, lost, reserve):
    answer = n

    rr = reserve.copy()
    for r in reserve:
        if r in lost:
            rr.remove(r)
            lost.remove(r)

    for l in lost:
        if l > 0 and l - 1 in rr:
            rr.remove(l - 1)
        elif l < answer and l + 1 in rr:
            rr.remove(l + 1)
        else:
            answer -= 1

    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
answer = solution(n, lost, reserve)
print(answer)