# 연습문제 > 정수 제곱근 판별
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

def solution(n):
    x = n ** 0.5
    return int((x+1) ** 2) if  x - int(x) == 0.0 else -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(121))    # 144
print(solution(3))    # -1

# 문제 풀이 시간: 12분

''' 더 좋은 코드
def solution(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1
'''
