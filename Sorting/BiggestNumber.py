from collections import deque


def solution(numbers):
    answer = ''

    numbers_str = deque(sorted([str(n) for n in numbers], reverse=True))

    while len(numbers_str) > 0:
        a = numbers_str.popleft()
        if len(numbers_str) > 0 and len(numbers_str[0]) != len(a):
            b, list = get_biggest_number(a, numbers_str)
            answer += b
            numbers_str = list
        else:
            answer += a

    return answer


def get_biggest_number(number, list):
    if list[0][-min(len(number), len(list[0]))] > number[-min(len(number), len(list[0]))] and list[0][:1] == number[:1]:
        b = list.popleft()
        a, new_list = get_biggest_number(b, list)
        new_list.appendleft(number)
        return a, new_list
    else:
        return number, list


# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
# numbers = [8, 80, 89, 70]
numbers = [90,908,89,898,10,101,1,8,9]
answer = solution(numbers)
print(answer)
