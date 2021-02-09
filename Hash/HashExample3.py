def solution(clothes):
    answer = 1
    dicClothes = {}
    for c in clothes:
        if c[1] in dicClothes.keys():
            dicClothes[c[1]] = dicClothes[c[1]] + 1
        else :
            dicClothes[c[1]] = 1
    print(dicClothes.values())
    for item in dicClothes.values():
        print(item)
        answer = answer * (item + 1)
    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

answer = solution(clothes)

print(answer)