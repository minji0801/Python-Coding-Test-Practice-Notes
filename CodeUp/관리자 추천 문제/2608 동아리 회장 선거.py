# 링크: https://codeup.kr/problem.php?id=2608

from itertools import product

n = int(input())
res = list(product(["O", "X"], repeat = n))

for a in res:
    print(''.join(a))

# 문제 풀이 시간: 6분
