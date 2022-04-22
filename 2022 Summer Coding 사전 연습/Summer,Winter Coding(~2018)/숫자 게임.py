# B 팀원들이 얻을 수 있는 최대 승점
# 한 명씩 수를 오픈했을 때, 더 큰 팀이 +1점
# 같은 숫자면 무승부

# def solution(A, B):
#     answer = 0
#     A.sort(reverse=True)

#     for i in range(len(A)):
#         a = A[i]
#         b = min(list(filter(lambda x: x > a,B)))
#         print(a, b)
#         B.remove(b)
#     return answer

''' 다른 사람의 풀이 
큰 값을 꺼내 b가 더 크면 통과, a가 더 크면 b를 다시 넣고 반복.
a와 b 둘 중 하나에서 원소가 안 남을 때까지 반복.
'''
import heapq
def solution(a, b):
    # 나중에 heappop으로 제일 작은 값을 꺼내기 위해서 부호 반전
    a = [-i for i in a]
    b = [-i for i in b]
    
    # a, b 리스트를 힙으로 변환
    heapq.heapify(a)
    heapq.heapify(b)
    
    answer = 0

    # a, b 모두 원소가 있을 때까지 반복(한쪽이라도 비면 종료)
    while b and a:
        # a, b에서 각각 제일 작은 값 꺼내기(원소가 모두 음수라서 제일 큰 값을 꺼내는 격)        
        am = heapq.heappop(a)
        bm = heapq.heappop(b)

        # b에서 꺼낸 값이 더 크면 +1
        if -am < -bm:
            answer += 1
        # b에서 꺼낸 값이 더 작으면 다시 넣기
        else:
            heapq.heappush(b, bm)
    return answer

print(solution([5,1,3,7],[2,2,6,8]))    # 3
# print(solution([2,2,2,2],[1,1,1,1]))    # 0

''' 더 좋은 풀이 
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer
'''
