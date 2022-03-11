# 연습문제 > 올바른 괄호
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3

def solution(s):
    n = 0
    for c in s:
        if c == "(":
            n += 1
        else:
            n -= 1
        if n < 0: break

    return True if n == 0 else False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("()()"))    # true
print(solution("(())()"))    # true
print(solution(")()("))    # false
print(solution("(()("))    # false
print(solution("(()))("))    # false

# 문제 풀이 시간: 10분

''' 더 좋은 코드
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0
'''
