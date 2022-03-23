# 2019 KAKAO BLIND RECRUITMENT > 실패율
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
# N: 전체 스테이지 수, stages: 사용자가 멈춰있는 스테이지 번호
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열 return
# 실패율이 같으면 스테이지 번호 낮은게 먼저
def solution(N, stages):
    answer = []
    for n in range(1, N+1):
        r = len([1 for s in stages if s >= n])    # 스테이지에 도달한 플레이어 수
        if r > 0:
            f = len([1 for s in stages if s == n]) / r
        else: 
            f = 0
        answer.append((n, f))
    
    answer.sort(key = lambda x : (-x[1], x[0]))
    return [a[0] for a in answer]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))    # [3,4,2,1,5]

# 문제 풀이 시간: 1시간 10분

''' 더 좋은 코드
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
'''
