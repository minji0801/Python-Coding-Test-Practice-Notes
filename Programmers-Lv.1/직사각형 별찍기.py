# 연습문제 > 직사각형 별찍기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12969

n, m = map(int, input().split())
for _ in range(m): print('*' * n)

# 풀이 시간: 3분

''' 더 좋은 코드
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
'''
