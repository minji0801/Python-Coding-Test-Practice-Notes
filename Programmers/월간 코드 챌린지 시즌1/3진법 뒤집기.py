# 월간 코드 챌린지 시즌1 > 3진법 뒤집기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3

def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)
    return int(answer, 3)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(45))    # 7
print(solution(125))    # 229

# 문제 풀이 시간: 6분
