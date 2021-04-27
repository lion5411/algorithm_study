def solution(name):
    answer = 0

    nameList = list(map(lambda x: ord(x) - ord("A") if ord(x) <= 77 else ord("Z") - ord(x) + 1, name))
    nameMap = [-1 if i > 0 else 0 for i in nameList]
    nameMap[0] = 0
    answer += nameList[0]
    cur = 0
    print(answer, nameList, ord("A"), ord("Z"))
    while -1 in nameMap:
        postIdx = nameMap.index(-1)
        postMove = calPosition(postIdx, cur, len(nameMap))
        preIdx = len(nameMap) - list(reversed(nameMap)).index(-1) - 1
        preMove =  calPosition(preIdx, cur, len(nameMap))
        print('+++++', nameMap)
        print(postIdx, preIdx, postMove, preMove)
        m = min(nameList[postIdx] + postMove, nameList[preIdx] + preMove)
        if m == nameList[postIdx] + postMove:
            print('----1')
            answer += (nameList[postIdx] + postMove)
            nameMap[postIdx] = 0
            cur = postIdx
        else:
            print('----2')
            answer += (nameList[preIdx] + preMove)
            nameMap[preIdx] = 0
            cur = preIdx
        print("r", m, answer, cur)
        print('+++++')

    return answer

def calPosition(i, j, length):
    if i > j:
        n = i - j
    else:
        n = j - i

    if length  / 2 < n:
        n = length - n
    return n

# name = "JEROEN"
# name = "JAN"
# name = "JAJAAAJ"
name = "ABAAAAAAABA"

answer = solution(name)
print(answer)