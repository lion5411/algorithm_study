import heapq


def solution(operations):
    answer = [0, 0]

    queue = []

    for o in operations:
        action = o.split(' ')
        if action[0] == 'I':
            heapq.heappush(queue, (int)(action[1]))
        elif o == 'D 1' and len(queue) > 0:
            a = heapq.nlargest(1, queue)
            queue.remove(a[0])
        elif o == 'D -1' and len(queue) > 0:
            a = heapq.heappop(queue)

    if len(queue) > 0:
        answer[0] = heapq.nlargest(1, queue)[0]
        answer[1] = heapq.nsmallest(1, queue)[0]

    return answer


# operations = ["I 16","D 1"]
# operations = ["I 7","I 5","I -5","D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

answer = solution(operations)
print(answer)
