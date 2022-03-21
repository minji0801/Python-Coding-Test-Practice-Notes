# 완전탐색 > 모의고사
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    a = [0, 0, 0]
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if n1[i % len(n1)] == answers[i]: a[0] += 1
        if n2[i % len(n2)] == answers[i]: a[1] += 1
        if n3[i % len(n3)] == answers[i]: a[2] += 1
    return [i+1 for i in range(len(a)) if a[i] == max(a)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1, 2, 3, 4, 5]))    # [1]
print(solution([1, 3, 2, 4, 2]))    # [1, 2, 3]

# 문제 풀이 시간: 23분
