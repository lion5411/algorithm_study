def solution(citations):
    answer = 0
    n = len(citations)
    sortedList = sorted(citations, reverse=True)

    for i in range(n, 1, -1):
        count = list(filter(lambda x: x >= i, sortedList))
        if len(count) >= i:
            answer = i
            break

    return answer


citations = [3, 0, 6, 1, 5]
answer = solution(citations)
print(answer)
