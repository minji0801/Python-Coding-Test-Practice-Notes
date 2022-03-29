# 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어
# 링크: https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

def solution(s):
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    s = s.lower()
    for i in range(len(word)):
        if s.isdigit(): break
        if word[i] in s: 
            s = s.replace(word[i], str(i))          
 
    return int(s)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("one4seveneight"))    # 1478
print(solution("23four5six7"))    #	234567
print(solution("2three45sixseven"))    # 234567
print(solution("123"))    #	123
print(solution("onezerothreezerothree"))

# 문제 풀이 시간: 19분

''' 다른 풀이 
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
'''
