# 연습문제 > 다음 큰 숫자
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3

def solution(n):
    num_one = str(format(n, 'b')).count('1')
    while True:
        n += 1
        if num_one == str(format(n, 'b')).count('1'): 
            break
    return n

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(78))    # 83
print(solution(15))    # 23

# 문제 풀이 시간: 12분

''' 더 좋은 코드
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n
'''
