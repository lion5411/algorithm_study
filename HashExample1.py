def solution(participant, completion):
    answer = ''
    hashMember = {}
    for c in completion:
        if c in hashMember:
            hashMember[c] = hashMember[c] + 1
        else:
            hashMember[c] = 1

    for c in participant:
        if c in hashMember:
            if hashMember[c] == 0:
                answer = c
                break
            else:
                hashMember[c] = hashMember[c] - 1
        else:
            answer = c
            break

    return answer


participant = ["eden", "kiki", "eden"];
completion = ["eden", "kiki"];

answer = solution(participant, completion);
print(answer)