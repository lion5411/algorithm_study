# Kruskal
def solution(n, costs):
    answer = 0

    island = [1] * n
    costs.sort(key=lambda x: x[2], reverse=True)
    s = DisjointSet(n)

    while len(costs) > 0:
        c = costs.pop()
        print(c, s, costs, island)
        r = s.union(c[0], c[1])
        if r:
            answer += c[2]

    return answer


# union find
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.n = n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        else:
            self.parent[y] = x
            return True


# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,8],[2,3,1]]

answer = solution(n, costs)
print(answer)