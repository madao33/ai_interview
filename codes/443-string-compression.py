from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        if N <= 1:
            return N
        prevCnt = 1
        left = 0
        for i in range(N):
            if i == N - 1 or chars[i] != chars[i+1]:
                chars[left] = chars[i]
                left += 1
                if prevCnt > 1:
                    for ch in str(prevCnt):
                        chars[left] = ch
                        left += 1
                prevCnt = 1
            else:
                prevCnt += 1
        return left


print(Solution().compress(["a","a","b","b","c","c","c"]))