# 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천
# 링크: https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,<>/]', '', new_id)
    new_id = re.sub('(([.])\\2{1,})', '.', new_id)
    if new_id.startswith('.'): new_id = new_id[1:]
    if new_id.endswith('.'): new_id = new_id[:-1]
    if not new_id: 
        new_id = "a"
    if len(new_id) > 15: 
        new_id = new_id[:15]
        if new_id.endswith('.'): new_id = new_id[:-1]
    elif len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]
    
    return new_id

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("...!@BaT#*..y.abcdefghijklm"))    # "bat.y.abcdefghi"
print(solution("z-+.^."))    # "z--"
print(solution("=.="))    # "aaa"
print(solution("123_.def"))    # "123_.def"
print(solution("abcdefghijklmn.p"))    # "abcdefghijklmn"
print(solution("aaaaaaaaaaaaaaaa"))    # "aaaaaaaaaaaaaaa"

# 문제 풀이 시간: 40분

''' 더 좋은 풀이
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''
