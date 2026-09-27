class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        i = 0
        j = i + k
        max_vals = []
        dq = deque([])
        count = 1

        for j in range(len(nums)):
            window = nums[i:j]
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
            if dq and i > dq[0]:
                dq.popleft()
            dq.append(j)
            count += 1
            if count > k:
                i += 1
                max_vals.append(nums[dq[0]])
            else:
                continue

        return max_vals