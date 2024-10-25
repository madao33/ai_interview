class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(x, parent):
            res = 0
            for edge in edges[x]:
                if edge[0] == parent:
                    continue
                res += edge[1] + dfs(edge[0], x)
            return res

        edges = [[] for _ in range(n)]
        for a, b in connections:
            edges[a].append([b, 1])
            edges[b].append([a, 0])
        
        return dfs(0, -1)


        
        