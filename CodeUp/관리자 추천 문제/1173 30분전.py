# 링크: https://codeup.kr/problem.php?id=1173

# h, m = 12, 35

h, m = map(int, input().split())

m -= 30
if m < 0:
    h -= 1
    m += 60
    if h < 0: h += 24

print(h, m)

# 문제 풀이 시간: 5분
