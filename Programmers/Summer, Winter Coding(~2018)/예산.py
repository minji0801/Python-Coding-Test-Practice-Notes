# Summer/Winter Coding(~2018) > 예산
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3

# d: 부서별 신청한 금액, budget: 예산
# 최대 몇 개의 부서에 물품을 지원할 수 있는지

def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if i > budget: break
        else:
            budget -= i
            answer += 1
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1,3,2,5,4], 9))    # 3
print(solution([2,2,3,3], 10))    # 4

# 문제 풀이 시간: 7분

''' 더 좋은 코드 (다만 효율성 부분 우려)
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
'''
