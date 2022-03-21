# 스택/큐 > 기능개발
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

# progresses: 진도, speeds: 개발 속도
# 각 배포마다 몇 개의 기능이 배포되는지 return
from math import ceil
def solution(progresses, speeds):
    answer = []
    date = [ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]

    count, now = 1, 0
    for d in date:
        if now == 0: now = d
        else :
            if now >= d: count += 1
            else:
                answer.append(count)
                count, now = 1, d
    answer.append(count)
                
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.

print(solution([93, 30, 55], [1, 30, 5]))    # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))    # [1, 3, 2]

# 문제 풀이 시간: 23분

''' 더 좋은 코드
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''
