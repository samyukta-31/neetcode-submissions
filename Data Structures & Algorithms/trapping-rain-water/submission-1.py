class Solution:
    def trap(self, height: List[int]) -> int:
        i = 1
        # j = 1
        # count = 1
        area = 0
        # prev_max = height[0]
        # mid_area = 0

        while i < len(height)-1:
            l = max(height[0:i])
            r = max(height[i+1:len(height)])
            area += max(min(l, r) - height[i], 0)
            i += 1

        # while j < len(height):
        #     if height[j] >= prev_max:
        #         area += mid_area
        #         mid_area = 0
        #         prev_max = height[j]
        #     else:
        #         mid_area += prev_max - height[j]
        #     j += 1
        # print(area)
        return area