# 전화번호 목록
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42577

# 접두어가 있으면 false, 없으면 true
def solution(phone_book):
    phone_book.sort()
    dic = {s:0 for s in phone_book}

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            dic[phone_book[i]] += 1
    return False if sum(dic.values()) > 0 else True

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["119", "97674223", "1195524421"]))    # false
print(solution(["123","456","789"]))    # true
print(solution(["12","123","1235","567","88"]))    # false
print(solution(["12", "3412"]))    # true

# 문제 풀이 시간: 47분

''' 더 좋은 코드
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
'''
