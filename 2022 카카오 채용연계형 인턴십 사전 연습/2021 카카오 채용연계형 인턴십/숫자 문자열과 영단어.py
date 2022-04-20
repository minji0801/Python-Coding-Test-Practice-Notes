words = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def solution(s):
    for word in words:
        if word in s:
            s = s.replace(word, str(words.index(word)))
    return int(s)

print(solution("one4seveneight"))    # 1478
print(solution("23four5six7"))    # 234567
print(solution("2three45sixseven"))    # 234567
print(solution("123"))    # 123

# 문제 풀이 시간: 6분
