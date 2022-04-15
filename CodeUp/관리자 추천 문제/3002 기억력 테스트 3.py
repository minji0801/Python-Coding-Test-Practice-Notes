# 링크: https://codeup.kr/problem.php?id=3002
# M개의 질문에 대해 그 숫자가 있었으면 그 숫자의 위치를 출력, 없었으면 -1을 차례대로 출력한다.

# n = 5
# nums = [2, 23, 55, 87, 100]
# m = 4
# ques = [5, 2, 100, 55]

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
ques = map(int, input().split())

def findNum(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

for n in ques:
    print(findNum(0, len(nums)-1, nums, n), end=' ')
