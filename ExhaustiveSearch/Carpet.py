from math import sqrt


def solution(brown, yellow):
    answer = []

    s = brown + yellow

    for i in range(1, int(sqrt(s)) + 1):
        if s % i == 0 and brown == 2 * (i + int(s / i) - 2):
            answer = [int(s / i), i]

    return answer


brown = 10
yelllow = 2
answer = solution(brown, yelllow)
print(answer)