# 연습문제 > 피보나치 수
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12945?language=python3

# n까지 반복하는데
# 앞의 두 원소의 합과 현재 원소의 합이다.

def solution(n):
    a = 0
    b = 1
    sum = 0
    for i in range(2, n+1):
        sum = a + b
        a = b
        b = sum
    return sum % 1234567


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3))    # 2
print(solution(5))    # 5

# 문제 풀이 시간: 17분
