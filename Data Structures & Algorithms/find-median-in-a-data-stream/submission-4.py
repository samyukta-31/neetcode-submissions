class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        import heapq
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        latest_small = -1*self.small[0] if self.small else None
        if not self.small:
            heapq.heappush(self.small, -1*num)
        else:
            if num > latest_small:
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -1*num)
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -1*heapq.heappop(self.large))
        elif len(self.large) + 1 < len(self.small):
            heapq.heappush(self.large, -1*heapq.heappop(self.small))

    def findMedian(self) -> float:
        n = len(self.small) + len(self.large)
        latest_small = self.small[0] if self.small else None
        latest_large = self.large[0] if self.large else None
        if n%2 == 0:
            median = (-1*latest_small + latest_large)/2
        else:
            median = -1*latest_small
        
        return median
        

        
        