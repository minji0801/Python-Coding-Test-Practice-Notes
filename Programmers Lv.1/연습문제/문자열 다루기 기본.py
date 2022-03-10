# 연습문제 > 문자열 다루기 기본
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3

# 길이가 4또는 6이고 숫자로만 구성되어 있으면 true
def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and s.isnumeric() else False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("a234"))    # false
print(solution("1234"))    # true

# 문제 풀이 시간: 5분

''' 더 좋은 코드
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
'''
