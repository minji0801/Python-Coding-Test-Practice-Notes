# 탐욕법(Greedy) > 구명보트
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42885

# 구명보트는 한 번에 2명씩 밖에 탈 수 없다.
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit
# 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값 return

def solution(people, limit):
    answer = 0
    people.sort()
    first, second = 0, len(people) - 1
    
    while first < second:
        if people[first] + people[second] <= limit:
            first += 1
            second -= 1
        else:
            second -= 1
        answer += 1

    # if first == second: answer += 1
        
    return answer + 1 if first == second else answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([70, 50, 80, 50], 100))    # 3
print(solution([70, 80, 50], 100))    # 3
print(solution([40,50,150,160], 200))    # 2
print(solution([100,500,500,900,950], 1000))    # 3
print(solution([50], 100))    # 1

# 문제 풀이 시간: 45분

''' 더 좋은 풀이
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
'''
