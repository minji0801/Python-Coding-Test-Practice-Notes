# 연습문제 > 소수 찾기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3

# 1부터 n 사이에 존재하는 소수의 개수
def solution(n):
    answer = 1
    for i in range(2, n+1):
        for j in range(1, int(i ** 0.5)+1):
            if j != 1 and i % j == 0:
                answer += 1
                break
    return n - answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(10))    # 4
print(solution(5))    # 3

# 문제 풀이 시간: 22분

''' 더 좋은 코드
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''
