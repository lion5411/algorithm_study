from collections import deque


def solution(priorities, location):
    answer = 0

    priorities = deque(priorities)

    while len(priorities) > 0:
        current = priorities.popleft()
        print('location', location, answer)
        for p in priorities:
            if p > current:
                priorities.append(current)
                print(current, priorities)
                current = None
                break
        if current is None:
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1

    return answer


# priorities = [2, 1, 3, 2]
# location = 2

priorities = [1, 1, 9, 1, 1, 1]
location = 0

answer = solution(priorities, location)
print(answer)
