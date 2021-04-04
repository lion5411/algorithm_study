def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    stu = [0, 0, 0]
    for i, an in enumerate(answers):
        if an == s1[i % 5]:
            stu[0] += 1
        if an == s2[i % 8]:
            stu[1] += 1
        if an == s3[i % 10]:
            stu[2] += 1
    answer = list(filter(lambda i: stu[i - 1] >= max(stu), [1, 2, 3]))

    return answer


# answers = [1,2,3,4,5]
answers = [1,3,2,4,2]

answer = solution(answers)
print(answer)