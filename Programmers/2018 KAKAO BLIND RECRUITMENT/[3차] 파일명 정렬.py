# 2018 KAKAO BLIND RECRUITMENT > [3차] 파일명 정렬
# 링크: https://programmers.co.kr/learn/courses/30/lessons/17686

# [head, number, tail]
def solution(files):
    split = {file:[] for file in files}
    answer = []
    index = 0
    str = ''

    for file in files:
        for char in file:
            if index == 0 and char.isdigit():    # 헤더 담기
                answer.append(str.lower())
                index += 1
                str = ''
            elif index == 1 and (not char.isdigit() or len(str) > 4 or file.index(char) == len(file)-1):
                if file.index(char) == len(file)-1:    # 마지막 글자면
                    answer.append(int(str+char))
                else:
                    answer.append(int(str))
                    index += 1
                    str = ''
            str += char
        answer.append(int(str) if str.isdigit() else str)
        print(answer)
        split[file] = answer
        answer = []
        index = 0
        str = ''
        
    # HEAD 사전 순 -> NUMBER 숫자 순
    split = sorted(split.items(), key=lambda x: (x[1][0], x[1][1]))
    return [s[0] for s in split]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))    # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))    # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

# print(solution(["foo9.txt", "foo010bar020.zip", "F-15", "MUZI01.zip", "muzi1.png"]))
print(solution(["img000012345", "img1.png","img2","IMG02"]))

# 문제 풀이 시간: 1시간 18분

''' 더 좋은 풀이(통과했지만 number가 5자리 이상일 경우 처리 안함)
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b
'''
