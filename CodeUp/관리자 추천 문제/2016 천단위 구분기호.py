# 링크: https://codeup.kr/problem.php?id=2016

# n = 8
# num = '12421421'

from math import ceil

n = int(input())
num = str(input())

res = []
for i in range(ceil(n/3)):
    if i == ceil(n/3)-1:
        res.insert(0, num)
        break
     
    res.insert(0, num[-3:])
    num = num[:-3]
    res.insert(0, ',')

print(''.join(res))

# 문제 풀이 시간: 15분
