import heapq


def solution(scoville, K):
    answer = 0

    if sum(scoville) == 0:
        return -1

    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) <= 0:
            answer = -1
            break
        second = heapq.heappop(scoville)

        answer += 1
        new = first + second * 2
        if new >= K:
            if second >= K:
                break
            else:
                heapq.heappush(scoville, new)
        else:
            heapq.heappush(scoville, new)


    return answer


# scoville = [1, 2, 3, 9, 10, 12]
# K = 7

scoville = [1, 2, 3]
K = 11

answer = solution(scoville, K)
print(answer)
