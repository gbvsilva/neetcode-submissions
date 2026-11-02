from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        visited = set()
        heap = [(0, k)]
        min_time = {node: float('inf') for node in range(1, n + 1)}
        min_time[k] = 0

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)

            for neighbor, t in graph[node]:
                new_time = time + t
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        if len(visited) == n:
            return max(min_time.values())
        return -1
                

