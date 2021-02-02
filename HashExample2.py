def solution(phone_book):
    answer = True

    phone_book.sort(reverse=True)

    while answer and len(phone_book) > 0:
        item = phone_book.pop()
        for p in phone_book:
            if p.startswith(item):
                answer = False
                break
    return answer

phone_book = ["11", "1"]

answer = solution(phone_book)

print(answer)