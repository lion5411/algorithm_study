def solution(number, k):
    answer = number
    loc = 0
    while k > 0:
        if loc == len(answer) - 1:
          if answer[loc-1] < answer[loc]:
              answer = answer[0:loc-1] + answer[loc:]
          else:
              answer = answer[0:loc]
          k -= 1
          loc = 0
        elif answer[loc] < answer[loc + 1]:
            answer = answer[0:loc] + answer[loc + 1:]
            k -= 1
            print(loc)
            if loc > 0:
                loc = loc - 1
            else:
                loc = 0
        else:
            loc += 1
    return answer

number = "4177252841"
k = 4

answer = solution(number, k)
print(answer)