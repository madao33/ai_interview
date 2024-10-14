class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)
        if N1 == 0:
            return True
        i, j = 0, 0
        while i < N1 and j < N2:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == N1:
                return True
        return False