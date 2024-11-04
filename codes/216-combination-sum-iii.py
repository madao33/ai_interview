from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(n, target, path):
            if n <= 0 or target <= 0:
                if n == 0 and target == 0:
                    res.append(path.copy())
                return
            start = 1 if len(path) == 0 else path[-1] + 1
            for num in range(start, 10):
                    path.append(num)
                    dfs(n-1, target-num, path)
                    path.pop(-1)
        
        dfs(k, n, [])
        return res

print(Solution().combinationSum3(3, 7))