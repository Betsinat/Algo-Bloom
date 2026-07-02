class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows, cols = len(grid),len(grid[0])
        def valid(x, y):
            return (0 <= x < rows and 0 <= y < cols)
        
        loss = [[float("inf")] * (cols) for _ in range(rows)]
        heap = [(grid[0][0], 0, 0)]
        loss[0][0] = grid[0][0]
    
        while heap:
            l, r, c = heappop(heap)
            if loss[r][c] < l:
                continue
            for dr,dc in dirs:
                nr, nc = dr + r, dc + c
                if not valid(nr, nc): continue
                cl = l + grid[nr][nc]
                if loss[nr][nc] > cl:
                    loss[nr][nc] = cl
                    heappush(heap, (cl, nr, nc))
        return health > loss[-1][-1]
