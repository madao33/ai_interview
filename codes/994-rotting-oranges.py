from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if not cnt:
            return 0
        ans = -1
        while q:
            length = len(q)
            for _ in range(length):
                cx, cy = q.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        cnt -= 1
            ans += 1
        if cnt:
            return -1
        return ans
    
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


