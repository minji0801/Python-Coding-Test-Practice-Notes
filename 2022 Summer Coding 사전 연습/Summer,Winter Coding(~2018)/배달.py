def solution(N, road, K):
    INF = int(1e9)
    graph = [[INF]*(N+1) for _ in range(N+1)]

    # 자기 자신으로 가는 비용은 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                graph[a][b] = 0

    # 마을이 이어진 길의 비용 초기화
    for a, b, c in road:
        graph[a][b] = min(c, graph[a][b])
        graph[b][a] = min(c, graph[b][a])
        
    # 점화식에 따라 플로이드 워셜 수행
    for k in range(1, N+1):    # k는 반드시 거쳐가는 마을
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    return len(list(filter(lambda x: x <= K, graph[1])))

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))    # 4
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))    # 4

# 문제 풀이 시간: 25분
