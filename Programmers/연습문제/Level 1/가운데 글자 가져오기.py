# 연습문제 > 가운데 글자 가져오기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
import math
def solution(s):
    return s[math.ceil(len(s)/2)-1:math.floor(len(s)/2)+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("abcde"))    # "c"
print(solution("qwer"))    # "we"
print(solution("qwerqwe"))    # "r"

# 문제 풀이 시간: 13분

''' 더 좋은 코드
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1
'''
