# 연습문제 > 행렬의 덧셈
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    answer = [[0 for _ in range(col)] for _ in range(row)]
    for r in range(row):
        for c in range(col):
            answer[r][c] = arr1[r][c] + arr2[r][c]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))    # [[4,6],[7,9]]
print(solution([[1],[2]], [[3],[4]]))    # [[4], [[6]]]

# 문제 풀이 시간: 22분

''' 더 좋은 코드
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
'''
