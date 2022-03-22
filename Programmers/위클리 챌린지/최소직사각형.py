# 위클리 챌린지 > 최소직사각형
# 링크: https://programmers.co.kr/learn/courses/30/lessons/86491

'''
1. 가로길이가 세로길이보다 작으면 서로 바꾸기
2. 가로, 세로 길이중 제일 긴거 뽑아서 서로 곱하기
'''
def solution(sizes):
    w, h = [], []
    for s in sizes:
        w.append(max(s))
        h.append(min(s))
    return max(w) * max(h)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))    # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))    # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))    # 133

# 문제 풀이 시간: 8분

''' 더 좋은 코드
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
'''
