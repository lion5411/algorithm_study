def solution(m, n, puddles):
    answer = 0
    r_map = [[0 for i in range(m)] for j in range(n)]
    for p in puddles:
        r_map[p[1]-1][p[0]-1] = -1
    print(r_map)

    for i in range(n):
        for j in range(m):
            if r_map[i][j] == -1:
                continue

            if i == 0 and j == 0:
                r_map[i][j] = 1
            elif i == 0 or r_map[i-1][j] == -1:
                if r_map[i][j-1] == -1:
                    r_map[i][j] = 0
                else:
                    r_map[i][j] = r_map[i][j-1]
            elif j == 0 or r_map[i][j-1] == -1:
                if r_map[i-1][j] == -1:
                    r_map[i][j] = 0
                else:
                    r_map[i][j] = r_map[i-1][j]
            else:
                r_map[i][j] = r_map[i][j-1] + r_map[i-1][j]
    answer = r_map[n-1][m-1] % 1000000007
    print(r_map)
    return answer


m = 4
n = 3
puddles = [[2, 2]]

answer = solution(m, n, puddles)
print(answer)