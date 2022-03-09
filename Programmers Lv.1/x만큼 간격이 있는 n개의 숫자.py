# 연습문제 > x만큼 간격이 있는 n개의 숫자
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = [x + (x * i) for i in range(n)]
    return answer

print(solution(2, 5))    # [2, 4, 6, 8, 10]
print(solution(4, 3))    # [4, 8, 12]
print(solution(-4, 2))    # [-4, -8]

# 문제 풀이 시간: 6분
