# 2017 팁스타운 > 예상 대진표
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12985

# 옆에 붙어있는 참가자랑 대결하는데, 다음 라운드에 올라가면 다시 1번 부터 번호를 배정한다.
# 토너먼트 방식이라 최종 1인이 남을 때까지 계속한다.
# n: 참가자 수
# a번 째 참가자가 b번째 참가자를 몇 번째 라운드에서 만날지

''' 질문하기 참고
일단 주의 하셔야 할 점이 홀수일때와 짝수일때를 구분하셔야 합니다 왜냐하면 만약 a = 4고 b = 5일때는 둘은 경쟁을 하지 않습니다 즉 a가 홀수일땐 b는 a+1이여야 하고 a가 짝수일 땐 b는 a-1이여야 합니다 그리고 a와 b의 값을 ceil값으로 2로 계속 나눠주면 되죠 이건 아마 다 아실테지만요....
'''
from math import ceil
def solution(n,a,b):
    answer = 0

    for i in range(n):
        a, b = ceil(a/2), ceil(b/2)
        answer += 1
        if a == b: break

    return answer

print(solution(8, 4, 7))    # 3

# 문제 풀이 시간: 44분

''' 더 좋은 풀이
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
'''
