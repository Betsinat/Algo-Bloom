class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def is_inbound(r, c):
            return min(r, c) >= 0 and max(r, c) < n

        def helper():
            q = deque()
            min_dist = {}

            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        q.append((r, c, 0))
                        min_dist[(r, c)] = 0

            while q:
                r, c, dist = q.popleft()

                for a, b in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if is_inbound(a, b) and (a, b) not in min_dist:
                        min_dist[(a, b)] = dist + 1
                        q.append((a, b, dist + 1))

            return min_dist

        min_dist = helper()

        maxHeap = [(-min_dist[(0, 0)], 0, 0)]
        visited = {(0, 0)}

        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -dist

            if (r, c) == (n - 1, n - 1):
                return dist

            for a, b in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if is_inbound(a, b) and (a, b) not in visited:
                    visited.add((a, b))
                    dist2 = min(dist, min_dist[(a, b)])
                    heapq.heappush(maxHeap, (-dist2, a, b))