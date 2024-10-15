class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, alti = 0, 0
        for n in gain:
            alti += n
            ans = max(ans, alti)
        return ans