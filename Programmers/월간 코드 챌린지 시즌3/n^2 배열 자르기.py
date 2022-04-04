# 월간 코드 챌린지 시즌3 > n^2 배열 자르기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/87390

'''
1. n행 n열 크기의 비어있는 2차원 배열을 만듭니다. [v]
2. i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다. [v]
3. 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다. [v]
4. 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다. [v]
5. 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다. []
'''

def solution(n, left, right):
    return [max(divmod(i, n))+1 for i in range(int(left), int(right+1))]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3, 2, 5))    # [3,2,2,3]
print(solution(4, 7, 14))    # [4,3,3,3,4,4,4,4]

# 문제 풀이 시간: 1시간 19분
# 질문하기 참고
