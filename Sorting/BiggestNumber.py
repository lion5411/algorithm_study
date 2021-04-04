def solution(numbers):
    answer = ''.join(sorted([str(n) for n in numbers], key=lambda x: x*3, reverse=True))

    return str(int(answer))



# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
# numbers = [8, 80, 89, 70]
numbers = [90,908,89,898,10,101,1,8,9]
answer = solution(numbers)
print(answer)
