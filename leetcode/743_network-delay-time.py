class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist={i:float('inf') for i in range(1,n+1)}
        heap=[(0,k)]
        road=defaultdict(list)
        for a,b,c in times:
            road[a].append((b,c))
        dist[k] = 0

        while heap:
            cur_dist,node = heapq.heappop(heap)#smallest

            if cur_dist > dist[node]:
                continue

            for neighbor,long1 in road[node]:
                new_dist = long1+ cur_dist
                if new_dist < dist[neighbor]:
                    dist[neighbor]=new_dist
                    heapq.heappush(heap,(new_dist,neighbor))

        max_dist = max(dist.values())
        return max_dist if max_dist != float('inf') else -1
