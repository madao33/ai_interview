from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(cur, target, curVal, graph, isVisited):
            if cur == target:
                return curVal
            res = -1.0
            isVisited.add(cur)
            for edge in graph[cur]:
                if edge[0] not in isVisited:
                    isVisited.add(edge[0])
                    res = dfs(edge[0], target, curVal * edge[1], graph, isVisited)
                    if res != -1.0:
                        break
            return res

        N = len(equations)
        graph = {}
        
        for i in range(N):
            a, b = equations[i]
            if a in graph:
                graph[a].append([b, values[i]])
            else:
                graph[a] = [[b, values[i]]]
            if b in graph:
                graph[b].append([a, 1.0/values[i]])
            else:
                graph[b] = [[a, 1.0/values[i]]]

        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
                continue
            isVisited = set()
            
            res.append(dfs(a, b, 1.0, graph, isVisited))

        return res
    
equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
querys = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
print(Solution().calcEquation(equations, values, querys))