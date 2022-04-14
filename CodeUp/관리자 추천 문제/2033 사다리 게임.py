# 링크: https://codeup.kr/problem.php?id=2033

k, n = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
p = int(input())

cp = p    # 현재 위치 번호

for d in data:
    if cp in d:
        cp = d[0] if d[0] != cp else d[1]
        
print(cp)

# 문제 풀이 시간: 16분
