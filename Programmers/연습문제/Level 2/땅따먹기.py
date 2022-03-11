# 연습문제 > 땅따먹기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3

def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[-1])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))    # 16

# 문제 풀이 시간: 30분

''' 더 좋은 코드
def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
'''
