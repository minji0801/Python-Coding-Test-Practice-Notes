# 연습문제 > 최대공약수와 최소공배수
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3

import math
def solution(n, m):
    gcd = math.gcd(n, m)
    return [gcd, n * m // gcd]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3, 12))    # [3, 12]
print(solution(2, 5))    # [1, 10]

# 문제 풀이 시간: 8분
