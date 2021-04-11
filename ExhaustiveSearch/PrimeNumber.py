from collections  import deque


def calNums(num):
    if num < 2:
        return 0
    for i in range(2, num // 2 + 1):
        # print(i, num, num % i)
        if num % i == 0:
            return 0
    print(num)
    return 1

def solution(numbers):
    answer = 0

    list1 = deque(numbers)

    numList = {}

    while len(list1) > 0:
        str = list1.popleft()
        if len(numList) > 0:
            numList = numList | set(str) | set(map(lambda x:  x + str, numList)) | set(map(lambda x: str + x, numList))
        else:
            numList = {str}

    nums = {int(n) for n in numList}
    print(list(filter(lambda x: x % 2 != 0, nums)))
    for i in nums:
        answer += calNums(i)
    return answer


# numbers = "17"
# numbers = "011"
numbers = "1276543"
answer = solution(numbers)
print(answer)