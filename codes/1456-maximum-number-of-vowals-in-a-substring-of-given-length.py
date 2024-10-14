class Solution:

    def isVowels(self, s: str) -> bool:
        return s in "aeiou"

    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        vowels = [1 if self.isVowels(s[i]) else 0 for i in range(N)]
        res = sum(vowels[:k])
        temp = res
        for i in range(k, N):
            temp += vowels[i]
            temp -= vowels[i-k]
            res = max(res, temp)
        return res