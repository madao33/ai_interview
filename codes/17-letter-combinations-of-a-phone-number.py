class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keymap = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def dfs(digits, idx, path, ans):
            if idx == len(digits):
                ans.append(path)
                return
            num = int(digits[idx])
            for ch in keymap[num-2]:
                dfs(digits, idx + 1, path + ch, ans)

        res = []
        if len(digits) == 0:
            return res
        dfs(digits, 0, "", res)
        return res