# 스택/큐 > 프린터
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42587

# priorities: 중요도, location: 인쇄를 요청한 문서의 위치
# 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return
def solution(priorities, location):
    answer = []
    index = [i for i, _ in enumerate(priorities)]
    
    while priorities:
        if priorities[0] < max(priorities):
            priorities.insert(len(priorities), priorities[0])
            index.insert(len(index), index[0])
            priorities.pop(0)
            index.pop(0)
        else:
            answer.append(index[0])
            priorities.pop(0)
            index.pop(0)

    return answer.index(location) + 1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([2, 1, 3, 2], 2))    # 1
print(solution([1, 1, 9, 1, 1, 1], 0))    # 5

# 문제 풀이 시간: 32분

''' 더 좋은 코드
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''
