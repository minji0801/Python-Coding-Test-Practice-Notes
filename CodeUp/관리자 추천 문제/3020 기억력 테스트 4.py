# n = 5
# nums = [23,5,32,87,50]
# m = 4
# ques = [5,2,100,87]

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
ques = list(map(int, input().split()))

dict = {nums[i]:i+1 for i in range(len(nums))}
for q in ques:
  if q in dict.keys():
    print(dict[q])
  else:
    print(-1)

# M개의 질문에 대해 그 숫자가 있었으면 그 숫자를 몇 번째로 불렀는지를 출력, 없었으면 -1을 하나씩 차례대로 출력한다.

# 문제 풀이 시간: 5분
