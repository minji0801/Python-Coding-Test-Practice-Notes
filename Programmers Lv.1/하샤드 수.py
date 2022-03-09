# 연습문제 > 하샤드 수
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    sum = 0
    for i in range(len(str(x))):
        sum += x // 10 ** i if i == len(str(x))-1 else (x // 10 ** i) % 10

    return True if x % sum == 0 else False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(10))    # true
print(solution(12))    # true
print(solution(11))    # false
print(solution(13))    # false

# 문제 풀이 시간: 19분

''' 더 좋은 코드
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0
'''
