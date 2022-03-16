# 정렬 > K번째수
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

# commands 각 원소 = [i, j, k]
# i부터 j까지 자르고 오름차순 정렬했을 때 k번째 수 구하기
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))    # [5, 6, 3]

# 문제 풀이 시간: 8분

''' 더 좋은 코드
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''
