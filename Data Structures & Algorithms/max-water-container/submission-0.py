class Solution:
    def maxArea(self, heights: List[int]) -> int:
        count = 0
        i = 0
        j = len(heights) - 1
        areas = []

        while i < len(heights):
            count = j-i
            if heights[i] > heights[j]:
                areas.append(min(heights[i], heights[j])*count)
                j -= 1
            else:
                areas.append(min(heights[j], heights[i])*count)
                i += 1
        return max(areas)
            


            