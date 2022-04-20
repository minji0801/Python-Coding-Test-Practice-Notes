# 서로 다른 3개를 골라 더했을 때 소수가 되는 경우

from itertools import combinations
def solution(nums):
    sum_of_three = list(map(sum, combinations(nums, 3)))
    answer = len(sum_of_three)

    for n in sum_of_three:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                answer -= 1
                break

    return answer

print(solution([1,2,3,4]))    # 1
print(solution([1,2,7,6,4]))    # 4

# 문제 풀이 시간: 7분
