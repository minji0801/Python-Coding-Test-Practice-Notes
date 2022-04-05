# 위클리 챌린지 > 모음사전
# 링크: https://programmers.co.kr/learn/courses/30/lessons/84512

# 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어
# word가 사전에서 몇 번째 단어인지 return
from itertools import product
def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    for i in range(1, 6):
        arr = map(lambda x: ''.join(x), product(alphabet, repeat = i))
        for s in arr: dictionary.append(s)

    return sorted(dictionary).index(word) + 1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("AAAAE"))    # 6
print(solution("AAAE"))    # 10
print(solution("I"))    # 1563
print(solution("EIO"))    # 1189

# 문제 풀이 시간: 16분
