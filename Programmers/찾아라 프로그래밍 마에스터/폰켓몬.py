# 찾아라 프로그래밍 마에스터 > 폰켓몬
# 링크: https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    n, t = len(nums) // 2, len(set(nums))
    return n if t >= n else t

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([3,1,2,3]))        # 2
print(solution([3,3,3,2,2,4]))    # 3
print(solution([3,3,3,2,2,2]))    # 2

# 문제 풀이 시간: 7분

''' 더 좋은 코드
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
'''
