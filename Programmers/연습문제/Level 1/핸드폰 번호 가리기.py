# 연습문제 > 핸드폰 번호 가리기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("01033334444"))    # "*******4444"
print(solution("027778888"))    # "*****8888"

# 문제 풀이 시간: 7분
