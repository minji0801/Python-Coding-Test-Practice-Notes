# 연습문제 > 나누어 떨어지는 숫자 배열
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3

# 나누어 떨어지는 값을 오름차순으로 정렬
# 하나도 없으면 [-1]
def solution(arr, divisor):
    result = sorted(filter(lambda x: x % divisor == 0, arr))
    return [-1] if not result else result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([5, 9, 7, 10],5))    # [5, 10]
print(solution([2, 36, 1, 3],1))    # [1, 2, 3, 36]
print(solution([3,2,6],10))    # [-1]

# 문제 풀이 시간: 6분

''' 더 좋은 코드
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''
