class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cntMap = dict()
        for a in arr:
            if a in cntMap:
                cntMap[a] += 1
            else:
                cntMap[a] = 1
        
        freqMap = set()
        for _, v in cntMap.items():
            if v in freqMap:
                return False
            else:
                freqMap.add(v)
        return True