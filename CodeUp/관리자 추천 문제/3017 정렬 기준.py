# n = 5
# data = {1: [100, 90], 2: [90, 100], 3: [80, 80], 4: [80, 90], 5: [60, 50]}

n = int(input())
data = dict()
for i in range(1, n+1):
  data[i] = list(map(int, input().split()))

res = sorted(data.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))

for r in res:
  print(r[0], r[1][0], r[1][1])

# 문제 풀이 시간: 11분
