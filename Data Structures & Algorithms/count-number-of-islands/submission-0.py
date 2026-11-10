class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() # keep tally of all seen islands
        Rows, Cols = len(grid), len(grid[0])
        island = 0

        def bfs(r, c):
            q = deque([(r, c)])
            seen.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if (nr, nc) not in seen and 0 <= nr < Rows and 0 <= nc < Cols and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        seen.add((nr, nc)) 

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    island += 1
        
        return island
