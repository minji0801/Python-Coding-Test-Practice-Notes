# 탐욕법(Greedy) > 체육복
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

# n: 전체 학생 수, lost: 체육복을 도난당한 학생 번호, reserve: 여벌의 체육복을 가져온 학생 번호
# 체육 수업을 들을 수 있는 학생의 최댓값 return
# (여벌 체육복을 가져온 학생도 체육복을 도난당했을 수 있다.)
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    c = 0
    lost, reserve = set(lost)-set(reserve), set(reserve)-set(lost)
    for i in lost:
        if i-1 not in reserve and i+1 not in reserve: continue
        else:
            if i-1 in reserve: reserve.remove(i-1)
            elif i+1 in reserve: reserve.remove(i+1)
            c += 1
    return n - (len(lost) - c)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(5, [2, 4], [1, 3, 5]))    # 5
print(solution(5, [2, 4], [3]))    # 4
print(solution(3, [3], [1]))    # 2
print(solution(3, [1, 2], [2, 3]))    # 2

# 문제 풀이 시간: 1시간 1분
