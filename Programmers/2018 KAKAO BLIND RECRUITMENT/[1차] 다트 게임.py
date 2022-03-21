# 2018 KAKAO BLIND RECRUITMENT > [1차]다트 게임
# 링크: https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3

import re
def solution(dartResult):
    answer = []
    for s, b in zip(re.findall('\d+', dartResult), re.findall('\D+', dartResult)):
        answer.append(bonus(int(s), b[0]))

        if len(b) == 2:
            if b[1] == '*':
                if len(answer) > 1: answer[-2] *= 2
                answer[-1] *= 2
            elif b[1] == '#': 
                answer[-1] = -answer[-1]
            
    return sum(answer)

def bonus(s, b):
    if b == 'S': return s
    elif b == 'D': return s ** 2
    elif b == 'T':  return s ** 3

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution('1S2D*3T'))    # 37
print(solution('1D2S#10S'))    # 9
print(solution('1D2S0T'))    # 3
print(solution('1S*2T*3S'))    # 23
print(solution('1D#2S*3S'))    # 5
print(solution('1T2D3D#'))    # -4
print(solution('1D2S3T*'))    # 59

# 문제 풀이 시간: 1시간

''' 더 좋은 코드
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

'''
