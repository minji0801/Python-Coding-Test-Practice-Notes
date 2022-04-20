def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill = list(skill)

    for st in skill_trees:
        st = list(filter(lambda x: x in skill,st))
        for i in range(len(st)):
            if st[i] != skill[i]:
                answer -= 1
                break

    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))    # 2

# 문제 풀이 시간: 32분
