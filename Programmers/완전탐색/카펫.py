# 완전탐색 > 카펫
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42842

# 카펫의 가로가 세로보다 길거나 같고
# 카펫의 가로 세로 의 곱이 갈색 노란색 격자의 합과 같으면 멈추기
def solution(brown, yellow):
    w, h = 3, 3
    while True:
        if isRight(w, h, brown, yellow): break
        else :
            w += 1
            h = 3
            while w >= h:
                if isRight(w, h, brown, yellow): break
                h += 1
    return [w, h]

def isRight(w, h, b, y):
    return True if w >= h and w * h == b + y and (w-2)*(h-2) == y else False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(10, 2))    # [4, 3]
print(solution(8, 1))    # [3, 3]
print(solution(24, 24))    # [8, 6]
print(solution(18, 6))    # [8, 3]

# 문제 풀이 시간: 49분

''' 더 좋은 코드
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
'''
