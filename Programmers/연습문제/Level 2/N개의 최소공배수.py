# 연습문제 > N개의 최소공배수
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3

# 배수 중 공통이 되는 가장 작은 수
import math
def solution(arr):
    # 처음부터 끝까지 gcd 값을 구해서 최종 최대공약수 구하기
    lcm = 0
    for i in range(1, len(arr)):
        # i = 0 일 때
        # arr[0]과 arr[1]의 최소공배수 구하기
        # i = 1일 때
        # 앞서 구한 최소공배수와 arr[2]의 최소공배수 구하기
        if i == 1 :
            lcm = arr[0]
        lcm = (lcm * arr[i]) // math.gcd(lcm, arr[i])
    return lcm

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([2, 6, 8, 14]))    # 168
print(solution([1, 2, 3]))    # 6
print(solution([3, 4, 9, 16]))    # 144
print(solution([2, 3, 4]))    # 12

# 문제 풀이 시간: 46분

''' 더 좋은 코드
from fractions import gcd

def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

'''
