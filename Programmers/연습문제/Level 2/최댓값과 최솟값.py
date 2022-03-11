# 연습문제 > 최댓값과 최솟값
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3

def solution(s):
    n = list(map(int, s.split(' ')))
    return str(min(n)) + " " + str(max(n))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("1 2 3 4"))    # "1 4"
print(solution("-1 -2 -3 -4"))    # "-4 -1"
print(solution("-1 -1"))    # "-1 -1"

# 문제 풀이 시간: 4분
