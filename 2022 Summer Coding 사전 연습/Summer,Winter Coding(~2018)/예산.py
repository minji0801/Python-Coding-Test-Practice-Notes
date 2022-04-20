# 최대 몇 개의 부서에 물품을 지원할 수 있는지

def solution(d, budget):
    answer = 0
    d.sort()
    for price in d:
        budget -= price
        if budget < 0:  break
        answer += 1
    return answer

print(solution([1,3,2,5,4], 9))    # 3
print(solution([2,2,3,3], 10))    # 4

# 문제 풀이 시간: 6분
