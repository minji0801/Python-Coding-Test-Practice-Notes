# 완전탐색 > 소수 찾기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42839

from math import floor
from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        p = set(map(''.join, permutations(list(numbers), i)))
        for n in list(map(int, p)):
            if n > 1 and isDecimal(n): answer.append(n)
    return len(set(answer))

def isDecimal(n):
    for i in range(1, floor(n ** 0.5)+1):
        if i != 1 and n % i == 0: return False
    return True

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("17"))    # 3
print(solution("011"))    # 2
print(solution("1231"))    #18
# [2, 3, 11, 13, 23, 31, 113, 131, 211, 311, 1123, 1213, 1231, 1321, 2113, 2131, 2311, 3121]

# 문제 풀이 시간: 38분

''' 더 좋은 코드
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
'''
