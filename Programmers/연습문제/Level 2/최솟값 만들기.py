# 연습문제 > 최솟값 만들기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12941?language=python3

def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    return sum([A[i] * B[i] for i in range(len(A))])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1, 4, 2], [5, 4, 4]))    # 29
print(solution([1, 2], [3, 4]))    # 10

# 문제 풀이 시간: 5분

''' 더 좋은 코드
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
'''
