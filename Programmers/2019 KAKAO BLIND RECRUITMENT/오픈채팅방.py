def solution(record):
    answer = []

    record = list(map(lambda x: x.split(), record))
    info = { r[1]:r[2] for r in record if len(r) == 3}

    for r in record:
        if r[0] == 'Enter':
            answer.append(f'{info[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(f'{info[r[1]]}님이 나갔습니다.')
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# 문제 풀이 시간 : 12분
