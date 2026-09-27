class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        neg_stones = [-1*val for val in stones]
        heapq.heapify(neg_stones)
        
        while len(neg_stones) > 1:
            print(neg_stones)
            y = heapq.heappop(neg_stones)
            x = heapq.heappop(neg_stones)
            heapq.heappush(neg_stones, y - x) if y != x else None
        return abs(neg_stones[-1]) if neg_stones else 0
        