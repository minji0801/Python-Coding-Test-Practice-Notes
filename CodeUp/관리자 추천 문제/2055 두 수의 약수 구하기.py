# 링크: https://codeup.kr/problem.php?id=2055

# a, b = 6, 14

a, b = map(int, input().split())

# 자기자신과 1은 무조건 포함
res = {1}
res.add(a)
res.add(b)

for i in range(2, int(a**0.5)+1):
    if a % i == 0:
        res.add(i)
        res.add(a // i)
        
for i in range(2, int(b**0.5)+1):
    if b % i == 0:
        res.add(i)
        res.add(b // i)

res = sorted(list(res))
print(' '.join(str(s) for s in res))

# 문제 풀이 시간: 17분
