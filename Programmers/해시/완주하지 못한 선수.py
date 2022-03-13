# 해시 > 완주하지 못한 선수
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

# 동명이인이 있을 수 있다.
def solution(participant, completion):
    dic = {p:0 for p in participant}
    for p in participant: dic[p] += 1
    for c in completion: dic[c] -= 1
    return sorted(dic.items(), key = lambda item: item[1], reverse = True)[0][0]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))    # "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))    # "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))    # "mislav"

# 문제 풀이 시간: 26분

''' 더 좋은 코드
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''
