def solution(routes):
    answer = 0

    sr = sorted(routes, key=lambda x: x[1])
    print(sr)
    checked = [0] * len(routes)
    while len(sr) > 0:
        print("aaa",sr)
        # l1 = list(filter(lambda x: x[0] <= sr[0][0] <= x[1], sr))
        l2 = list(filter(lambda x: x[0] <= sr[0][1] <= x[1], sr))
        # print(l1, l2)
        # if len(l1) >= len(l2):
        #     for l in l1:
        #         sr.remove(l)
        # else:
        for l in l2:
            sr.remove(l)
        answer += 1

    return answer


route = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
# route = [[2, 2],[0, 1],[-10,9]]

answer = solution(route)
print(answer)