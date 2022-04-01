# 2022 KAKAO BLIND RECRUITMENT > 주차 요금 계산
# 링크: https://programmers.co.kr/learn/courses/30/lessons/92341

# fees: 요금표 (기본 시간, 기본 요금, 단위 시간, 단위 요금)
# records: 입/출차 기록 (시각, 차량 번호, 내역)
from math import ceil
def solution(fees, records):
    records = [record.split(' ') for record in records]
    dic = {record[1]: [] for record in records}

    # 차량 번호 별 입/출차 시각 딕셔너리 만들기
    for record in records:
        time = list(map(int, record[0].split(':')))
        dic[record[1]].append([time[0], time[1]])

    # 출차 기록이 없으면 '23:59' 추가하기
    for _, time in dic.items():
        if len(time) % 2 == 1: time.append([23, 59])

    # 총 주차시간 구하기
    for num, time in dic.items():
        entry = []
        parking = 0
        
        for i in range(len(time)):
            t = time[i]
            if i % 2 == 0: # 입차
                entry = t
            else: # 출차
                exit = t
                h, m = exit[0]-entry[0], exit[1]-entry[1]
                parking += (h * 60) + m
        dic[num] = parking

    # 주차 요금 구하기
    for num, time, in dic.items():
        default_time, base_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
        if time <= default_time: # 기본 요금
            dic[num] = base_fee
        else: # 기본 요금 + 추가 요금
            print(base_fee, time, default_time, unit_time, unit_fee)
            dic[num] = int(base_fee + ceil((time-default_time) / unit_time) * unit_fee)

    dic = sorted(dic.items(), key=lambda x: x[0])
        
    return [fee for num, fee in dic]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))    # [14600, 34400, 5000]

# 문제 풀이 시간: 1시간 11분
