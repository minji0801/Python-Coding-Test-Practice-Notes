# 해시 > 위장
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42578

# [의상 이름, 의상 종류]

def solution(clothes):
    answer = 1
    dic = {c[1]:[] for c in clothes}
    for c in clothes: dic[c[1]].append(c[0])
    for v in dic.values(): answer *= (len(v)+1)
    return answer - 1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))    # 5
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))    # 3
print(solution([["a", "a"], ["b", "b"], ["c", "c"]]))    # 7

# 문제 풀이 시간: 58분

''' 다른 코드
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''
