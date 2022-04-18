# b = 40
# n = 6
# p = [7,13,17,19,29,31]

b = int(input())
n = int(input())
p = list(map(int, input().split()))

from itertools import combinations

res = 0
for i in range(1, n+1):
  c = list(filter(lambda x: x <= b, map(sum, combinations(p, i))))
  if c and res < max(c):
    res = max(c)

print(res)

# 문제 풀이 시간: 22분
