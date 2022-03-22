# 월간 코드 챌린지 시즌3 > 나머지가 1이 되는 수 찾기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/87389?language=python3

def solution(n):
    x = 1
    while True:
        if n % x == 1:
            return x
        else:
            x += 1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(10))    # 3
print(solution(12))    # 11

# 문제 풀이 시간: 4분
