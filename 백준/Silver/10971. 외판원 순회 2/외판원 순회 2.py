import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 도시의 개수와 비용 행렬 입력 받기
도시_개수 = int(input().strip())
비용행렬 = [list(map(int, input().split())) for _ in range(도시_개수)]

무한대 = float('inf')
# 최소비용_메모[방문_상태][현재도시]는 해당 방문 상태에서 현재 도시까지 도달하는 최소 비용
최소비용_메모 = [[None] * 도시_개수 for _ in range(1 << 도시_개수)]

def 외판원순회(방문_상태, 현재도시):
    # 모든 도시를 방문한 경우, 현재 도시에서 출발 도시(0번)로 돌아가는 비용을 반환
    if 방문_상태 == (1 << 도시_개수) - 1:
        return 비용행렬[현재도시][0] if 비용행렬[현재도시][0] != 0 else 무한대

    # 이미 계산한 경우, 저장된 값을 반환
    if 최소비용_메모[방문_상태][현재도시] is not None:
        return 최소비용_메모[방문_상태][현재도시]

    최소비용 = 무한대
    # 아직 방문하지 않은 모든 도시를 시도해본다.
    for 다음도시 in range(도시_개수):
        # 다음 도시가 아직 방문되지 않았고, 현재 도시에서 다음 도시로 갈 수 있다면
        if 방문_상태 & (1 << 다음도시) == 0 and 비용행렬[현재도시][다음도시] != 0:
            최소비용 = min(최소비용, 외판원순회(방문_상태 | (1 << 다음도시), 다음도시) + 비용행렬[현재도시][다음도시])
    
    최소비용_메모[방문_상태][현재도시] = 최소비용
    return 최소비용

# 0번 도시에서 시작하여 모든 도시를 방문하는 최소 비용 출력
print(외판원순회(1, 0))
