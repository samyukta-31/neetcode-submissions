class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {num:0 for num in nums}

        for num in nums:
            h[num] += 1
            if h[num] > 1:
                return True
        return False