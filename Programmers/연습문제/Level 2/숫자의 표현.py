# 연습문제 > 숫자의 표현
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12924

# 연속한 자연수로 표현하는 방법의 수
import math
def solution(n):
    count = 1
    for i in range(1, math.ceil(n / 2)):
        sum = 0
        while sum <= n:
            if sum == n: 
                count += 1
                break
            sum += i
            i += 1
            
    return count

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(15))    # 4

# 문제 풀이 시간 : 13분

''' 더 좋은 코드
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
'''
