# 연습문제 > 문자열 내 p와 y의 개수
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3

# p와 y의 개수가 같으면 true (p, y가 하나도 없어도)
from collections import Counter

def solution(s):
    c = Counter(s.lower())
    return True if c['p'] == c['y'] else False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("pPoooyY"))    # true
print(solution("Pyy"))    # false

# 문제 풀이 시간: 10분

''' 더 좋은 코드
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
'''
