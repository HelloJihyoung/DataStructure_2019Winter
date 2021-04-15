def solution(phone_book):
    phone_book.sort()
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num2.startswith(num1):
            return False
    return True

def solution(phone_book):
    hash = {}
    # 종류를 해시에 넣어줌
    for num in phone_book:
        hash[num] = 1
    
    for num in phone_book:
        # num : 원소 하나씩
        # 비교위한 임시저장소
        temp = ""
        # 원소 하나에 글자 하나씩
        for i in num:
            # temp에 접두어 저장
            temp += i
            # 저장한 접두어가 hash에 존재할 경우 단, 접두어가 현재 보는 단어일때 예외
            if temp in hash and temp != num:
                return False
    return True

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))