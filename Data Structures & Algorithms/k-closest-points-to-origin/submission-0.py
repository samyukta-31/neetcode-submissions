class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        distances = []
        heapq.heapify(distances)

        for x, y in points:
            distance = (x**2 + y**2)**0.5
            heapq.heappush(distances, [distance, [x,y]])
        
        i = 0
        top_k = []
        while i < k:
            top_k.append(heapq.heappop(distances)[1])
            i += 1

        return top_k