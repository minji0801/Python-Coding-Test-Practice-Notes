# 2019 카카오 개발자 겨울 인턴십 > 튜플
# 링크: https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

# def solution(s):
#     answer = []

#     # s가 문자열이니까 리스트로 변환하기
#     s = s.strip('{''}').split('},{')
#     s = list(map(lambda x: x.split(','), s))
#     s.sort(key=lambda x: len(x))

#     # 리스트 수 만큼 반복하기
#     # answer에 원소가 없는 경우만 넣기
#     for i in range(len(s)):
#         for n in s[i]:
#             if n not in answer:
#                 answer.append(n)
#     return list(map(int, answer))

''' 또 다른 풀이'''
import re
def solution(s):
    # s가 문자열이니까 리스트로 변환하기
    s = re.sub('[{}]', '', s).split(',')
    s = list(map(int, s))

    dic = {n:0 for n in set(s)}
    # # 각 문자가 나온 횟수 카운트하기
    for n in s:
        dic[n] += 1
    
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return [k for k, v in dic]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))    # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))    # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))    # [111, 20]
print(solution("{{123}}"))    # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))    # [3, 2, 4, 1]

# 문제 풀이 시간: 30분

''' 더 좋은 풀이
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
'''
