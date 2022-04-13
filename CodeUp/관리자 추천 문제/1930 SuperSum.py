# 링크: https://codeup.kr/problem.php?id=1930

def superSum(k, n):
    if k == 0:
        memo[k][n] = n

    if memo[k][n] == -1:
        res = 0
        for i in range(1, n + 1):
            res += superSum(k - 1, i)
        memo[k][n] = res
        
    return memo[k][n]
    
while True:
    try:
        k, n = map(int, input().split())
        memo = [[-1 for _ in range(n + 1)] for _ in range(k + 1)]
        print(superSum(k, n))
    except EOFError:
        break

# 문제 풀이 시간: 1시간
