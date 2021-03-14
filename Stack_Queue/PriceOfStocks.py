from collections import deque

def solution(prices):
    answer = []

    prices_queue = deque(prices)
    length = len(prices_queue)

    while length > 0:
        price = prices_queue.popleft()
        length -= 1
        count = 0
        for p in prices_queue:
            count += 1
            if (p < price) or (count == length):
                answer.append(count)
                break
    answer.append(0)

    return answer


prices = [1, 2, 3, 2, 3]

answer = solution(prices)
print(answer)
