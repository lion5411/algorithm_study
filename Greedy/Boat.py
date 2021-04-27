from collections import deque


def solution(people, limit):
    answer = 0

    p = deque(sorted(people, reverse=True))

    while len(p) > 0:
        cur = p.popleft()
        if len(p) > 0 and cur + p[-1] <= limit:
            p.pop()
        answer += 1

    return answer

# people = [70, 50, 80, 50]
# limit = 100
# people = [40, 40, 20]
# limit = 100
people = [80, 20, 50, 50]
limit = 100
answer = solution(people, limit)
print(answer)