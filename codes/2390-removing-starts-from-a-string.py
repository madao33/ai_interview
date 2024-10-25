class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch != '*':
                ans.append(ch)
            else:
                ans.pop()
        return ''.join(ans)