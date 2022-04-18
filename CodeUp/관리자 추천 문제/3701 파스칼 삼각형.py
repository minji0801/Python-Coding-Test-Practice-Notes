# n = 5
n = int(input())

prev = [1]
for i in range(1, n+1):
  arr = [1] * i

  for j in range(1, len(arr)-1):
    arr[j] = prev[j-1]+prev[j]

  prev = arr
  print(' '.join(map(str, prev)) + ' ')

# 문제 풀이 시간: 13분
