# 연습문제 > 시저 암호
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3

# 리스트로 만들고 각 문자를 유니코드로 변환하기
# 1 <= n <= 25
# 공백: 32 -
# 대문자: 65 ~ 90
# 소문자: 97 ~ 122

def solution(s, n):
    result = ""
    
    for i in list(ord(c) for c in s):
        if i == 32:
            result += " "
        elif 65 <= i <= 90:
            if i + n > 90:
                result += chr(i + n - 26)
            else:
                result += chr(i + n)
        elif 97 <= i <= 122:
            if i + n > 122:
                result += chr(i + n - 26)
            else:
                result += chr(i + n)
            
    return result 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("AB", 1))    # "BC"
print(solution("z", 1))    # "a"
print(solution("a B z", 4))    # "e F d"

# 문제 풀이 시간: 45분

''' 더 좋은 코드
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
'''
