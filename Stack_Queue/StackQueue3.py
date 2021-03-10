from collections import deque


def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)
    i = 0
    while len(progresses) > 0:
        if progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            i += 1
        else:
            if i > 0:
                answer.append(i)
                i = 0
            for p in range(len(progresses)):
                progresses[p] = progresses[p] + speeds[p]
    answer.append(i)

    return answer


# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

progresses = [99, 99, 99]
speeds = [1, 1, 1]

answer = solution(progresses, speeds)
print(answer)
