from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [False for i in range(N)]
        keys = deque()
        visited[0] = True
        for key in rooms[0]:
            keys.append(key)
        
        while keys:
            length = len(keys)
            for i in range(length):
                key = keys.popleft()
                if not visited[key]:
                    visited[key] = True
                    for j in rooms[key]:
                        keys.append(j)
            
        return sum(visited) == N
                