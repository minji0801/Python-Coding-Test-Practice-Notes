# 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시
# 링크: https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3

# 캐시 크기(cacheSize)와 도시이름 배열(cities)
# 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.
# 총 실행시간 출력
# cache hit(존재하면)은 1, cache miss(존재하지 않으면)는 5

''' 
1. 크기가 cacheSize 인 배열을 만든다.
2. cities를 소문자로 바꾼다.
3. 도시를 배열에 넣는데, 존재하지 않으면 +5하고 제일 뒤에 넣는다.
4. 존재하면 +1하고 이미 있는 도시를 제거 후 제일 뒤에 넣는다.
'''
def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = list(map(lambda city: city.lower(), cities))

    if cacheSize == 0: return len(cities) * 5

    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5
            if len(cache) == cacheSize: cache.pop()
        cache.insert(0, city)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))    # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))    # 21
print(solution(0, ["LA", "LA"]))    # 10

# 문제 풀이 시간: 23분

''' 더 좋은 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
'''
