# 월간 코드 챌린지 시즌1 > 두 개 뽑아서 더하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    return sorted(list(answer))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([2,1,3,4,1]))    # [2,3,4,5,6,7]
print(solution([5,0,2,7]))

# 문제 풀이 시간: 7분
