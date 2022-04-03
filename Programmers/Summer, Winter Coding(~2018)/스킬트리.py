# Summer/Winter Coding(~2018) > 스킬트리
# 링크: https://programmers.co.kr/learn/courses/30/lessons/49993

# 선행 스킬 순서 skill, 유저들이 만든 스킬트리를 담은 배열 skill_trees
# 가능한 스킬 트리 개수 return

# 1. skill_trees를 skill에 있는 단어로만 추린다.
# 2. skill을 딕셔너리로 정리한다.{인덱스 번호: 스킬이름}
# 3. skill_trees에 인덱스를 비교해서 동일한 것만 센다.

def solution(skill, skill_trees):
    dic = {s:skill.index(s) for s in skill}
    answer = len(skill_trees)

    def isInSkill(skill_tree):
        result = ''
        for char in skill_tree:
            if char in skill:
                result += char
        return result

    for skill_tree in skill_trees:
        skill_tree = isInSkill(skill_tree)
        for char in skill_tree:
            if dic[char] != skill_tree.index(char):
                answer -= 1
                break
        
    return answer    

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))    # 2

# 문제 풀이 시간: 22분

''' 더 좋은 풀이
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
'''
