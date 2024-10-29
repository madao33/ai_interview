from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.set = SortedSet(range(1, 1001))


    def popSmallest(self) -> int:
        temp = self.set[0]
        self.set.remove(temp)
        return temp

    def addBack(self, num: int) -> None:
        self.set.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)