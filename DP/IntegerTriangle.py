
def solution(triangle):
    t_map = list(map(lambda x: [0]*len(x), triangle))
    print(t_map)
    i = 0
    j = 0
    for tr in triangle:
        for t in tr:
            print(t, i, j)
            t_map[i][j] = getNij(t_map, i, j, t)
            j += 1
            print(t_map)
        i += 1
        j = 0
    answer = max(t_map[len(triangle) - 1])
    return answer


def getNij(map, i, j, x):
    if i == 0 and j == 0:
        r = x
    elif j == 0:
        r = map[i-1][j] + x
    elif j == i:
        r = map[i-1][j-1] + x
    else:
        r = max(map[i-1][j-1] + x, map[i-1][j] + x)
    return r


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

answer = solution(triangle)
print(answer)