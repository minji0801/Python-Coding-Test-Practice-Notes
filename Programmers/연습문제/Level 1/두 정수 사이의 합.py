# 연습문제 > 두 정수 사이의 합
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3

def solution(a, b):
    return sum(i for i in range(min(a, b), max(a, b)+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3, 5))    # 12
print(solution(3, 3))    # 3
print(solution(5, 3))    # 12

# 문제 풀이 시간: 5분

''' 더 좋은 코드
def adder(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))
'''
