# 연습문제 > 약수의 합
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(12))    # 28
print(solution(5))    # 6

# 문제 풀이 시간: 6분

''' 더 좋은 코드
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])
'''
