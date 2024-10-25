class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowCnt = Counter(tuple(row) for row in grid)
        return sum(rowCnt[col] for col in zip(*grid))