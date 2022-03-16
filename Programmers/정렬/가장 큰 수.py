# 정렬 > 가장 큰 수
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers.sort(key=lambda x:(str(x)*4)[0:4], reverse=True)
    return str(int(''.join(map(str, numbers))))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([6, 10, 2]))    # "6210"
print(solution([3, 30, 34, 5, 9]))    # "9534330"
print(solution([1, 10, 100, 1000]))    # "1101001000"
print(solution([21, 212]))
print(solution([0, 0, 0, 0]))

# 문제 풀이 시간: 1시간 20분

''' 더 좋은 코드
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
'''
