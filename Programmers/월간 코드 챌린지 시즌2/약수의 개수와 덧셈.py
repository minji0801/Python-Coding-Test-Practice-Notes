# 월간 코드 챌린지 시즌2 > 약수의 개수와 덧셈
# 링크: https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3

# left부터 right까지 약수의 개수가 짝수인 수는 더하고
# 홀수인 수는 빼기

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0: count += 1
    
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(13, 17))    # 43

# 문제 풀이 시간: 7분

''' 더 좋은 코드
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''
