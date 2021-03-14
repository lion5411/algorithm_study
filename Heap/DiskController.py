import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)

    newJobs = []
    for item in jobs:
        heapq.heappush(newJobs, (item[0], item[1]))

    total = 0
    time = 0
    while len(newJobs) > 0:
        if newJobs[0][0] <= time:
            heap = []
            while len(newJobs) > 0 and newJobs[0][0] <= time:
                j = heapq.heappop(newJobs)
                if j[0] <= time:
                    heapq.heappush(heap, (j[1], j[0]))

            h = heapq.heappop(heap)
            total += (time - h[1] + h[0])
            time += h[0]
            while len(heap) > 0:
                h = heapq.heappop(heap)
                heapq.heappush(newJobs, (h[1], h[0]))

        else:
            time += 1

    answer = (int)(total / length)
    return answer



jobs = [[0, 10], [2, 10], [9, 10], [15, 2]] #14
# jobs = [[0, 10], [2, 12], [9, 19], [15, 17]] #25
# jobs = [[0, 3], [1, 9], [2, 6]] #9
# jobs = [[0, 1]] #1
# jobs = [[1000, 1000]] #1000
# jobs = [[0, 1], [0, 1], [0, 1]] #2
# jobs = [[0, 1], [0, 1], [0, 1], [0, 1]] #2
# jobs = [[0, 1], [1000, 1000]] #500
# jobs = [[100, 100], [1000, 1000]] #500
# jobs = [[10, 10], [30, 10], [50, 2], [51, 2]] #6
# jobs = [[0, 3], [1, 9], [2, 6], [30, 3]] #7
answer = solution(jobs)
print(answer)
