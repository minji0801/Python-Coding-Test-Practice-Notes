# n, m = 6, 3
# nums = [3,5,2,1,4,3]
# ques = [[2,4],[1,1],[1,3]]

n, m = map(int, input().split())
nums = list(map(int, input().split()))
ques = [list(map(int, input().split())) for _ in range(m)]

for i in range(1,len(nums)):
    nums[i] += nums[i-1]

for q in ques:
    a = nums[q[1]-1]
    b = nums[q[0]-2] if q[0]-2 >= 0 else 0
    print(a-b)

'''
3 5 2 1 4 3 
3 8 10 11 15 18
'''

# 문제 풀이 시간: 20분
