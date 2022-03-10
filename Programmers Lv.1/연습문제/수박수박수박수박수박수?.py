# 연습문제 > 수박수박수박수박수박수?
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3

def solution(n):
    return "수박" * (n // 2) if n % 2 == 0 else "수박" * (n // 2) + "수"

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3))    # "수박수"
print(solution(4))    # "수박수박"

# 문제 풀이 시간: 5분

''' 더 좋은 코드
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

def water_melon(n):
    return ("수박"*n)[0:n]
'''
