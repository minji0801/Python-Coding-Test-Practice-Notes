# 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3

'''
이용자의 ID가 담긴 문자열 배열 id_list, 
각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 
정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 
각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return
'''
def solution(id_list, report, k):
    report = [r.split(' ') for r in set(report)]
    count = {i: 0 for i in id_list}
    info = {i: [] for i in id_list}

    # u: 신고한 유저, r: 신고당한 유저
    for u, r in report:
        count[r] += 1
        info[u].append(r)

    count = dict(filter(lambda x: x[1] >= k, count.items()))

    for u, r in info.items():
        mail = 0
        for n in r:
            if n in count.keys(): mail += 1
        id_list[id_list.index(u)] = mail
    
    return id_list

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))    # [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)) # [0, 0]

# 문제 풀이 시간: 26분

''' 더 좋은 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
'''
