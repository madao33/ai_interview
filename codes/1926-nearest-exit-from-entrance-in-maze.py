class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            cx, cy, d = q.popleft()
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return d + 1
                    maze[nx][ny] = '+'
                    q.append((nx, ny, d + 1))
        return -1