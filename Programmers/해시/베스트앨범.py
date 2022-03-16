# 해시 > 베스트앨범
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42579

# 장르별 가장 많이 재생된 노래를 두 개씩 모아서 
def solution(genres, plays):
    answer = []
    num = {g:0 for g in genres}    # 장르별 총 재생 횟수
    info = {g:{} for g in genres}    # 장르별 재생 정보 {순서:재생횟수}

    for g, p, i in zip(genres, plays, range(len(genres))):
        num[g] += p
        info[g][i] = p

    num = sorted(num.items(), key=lambda x:x[1], reverse=True)
    for g, _ in list(num):
        n = sorted(info[g].items(), key=lambda x:x[1], reverse=True)
        count = 1
        for i, _ in n:
            if count > 2: break
            answer.append(i)
            count += 1
    
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))    # [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500]))    # [4, 1, 0, 2]    같은건 앞에꺼
print(solution(["classic", "pop", "pop"], [800, 600, 2500]))    # [2, 1, 0]    곡이 하나면 하나만

# 문제 풀이 시간: 1시간 14분

''' 참고한 코드
def solution(genres, plays):
    genres_sum = {}
    plays_sum = {}
    for i in range(len(genres)):
        if genres[i] in genres_sum:
            genres_sum[genres[i]] += plays[i]
            plays_sum[genres[i]][i] = plays[i]       
        else:
            genres_sum[genres[i]] = plays[i]
            plays_sum[genres[i]] = {i:plays[i]}
    genres_sum = sorted(genres_sum.items(), key = (lambda x: x[1]), reverse = True)
    answer = []
    for (genre, _) in list(genres_sum):
        x = sorted(plays_sum[genre].items(), key = (lambda x: x[1]),reverse = True)
        count = 1
        for (i, _) in x:
            if count < 3:
                answer.append(i)
                count += 1
            else:
                break
    return answer
'''

''' 더 좋은 코드
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
'''
