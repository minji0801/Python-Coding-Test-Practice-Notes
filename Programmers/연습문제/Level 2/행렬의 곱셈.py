# 연습문제 > 행렬의 곱셈
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3

import numpy
def solution(arr1, arr2):
    return numpy.dot(arr1, arr2).tolist()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))    # [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))    # [[22, 22, 11], [36, 28, 18], [29, 20, 14

# 문제 풀이 시간: 10분

''' 더 좋은 코드
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
'''
