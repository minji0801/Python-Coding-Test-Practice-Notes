# 연습문제 > 같은 숫자는 싫어
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    answer = []
    n = -1
    for i in arr:
        if n != i:
            answer.append(i)
        n = i  
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1,1,3,3,0,1,1]))    # [1, 3, 0, 1]
print(solution([4,4,4,3,3]))    # [4, 3]

# 문제 풀이 시간: 10분

''' 더 좋은 코드
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
'''
