class MedianFinder:

    def __init__(self):

        self.small = []  # max heap (store negatives)

        self.large = []  # min heap


    def addNum(self, num: int) -> None:

        # 1. Add to small (as negative for max-heap behavior)

        heapq.heappush(self.small, -num)


        # 2. Move the largest of small into large

        heapq.heappush(self.large, -heapq.heappop(self.small))


        # 3. Rebalance if large grew too big

        if len(self.large) > len(self.small):

            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:

        if len(self.small) > len(self.large):

            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2