# 건전지 사용량의 최솟값

def solution(n):
    ans = 0
    while n > 0:
        s, r = divmod(n, 2)
        n = s
        if r % 2 == 1:
            ans += 1

    return ans

print(solution(5))    # 2
print(solution(6))    # 2
print(solution(5000))    # 2
print(solution(1000000000))    # 2

# 문제 풀이 시간: 32분

''' 더 좋은 코드
def solution(n):
    return bin(n).count('1')
'''
