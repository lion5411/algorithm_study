def solution(money):
    sum1 = [0] * len(money)
    sum2 = [0] * len(money)

    sum1[0] = money[0]
    sum1[1] = sum1[0]

    sum2[0] = 0
    sum2[1] = money[1]

    for i in range(2, len(money)):
        if i == len(money) - 1:
            sum1[i] = max(sum1[i-1], sum1[i-2])
        else:
            sum1[i] = max((sum1[i-2] + money[i]), sum1[i-1])

        sum2[i] = max((sum2[i-2] + money[i]), sum2[i-1])

    answer = max(sum1[-1], sum2[-1])
    return answer


money = [1, 2, 3, 1]

answer = solution(money)
print(answer)