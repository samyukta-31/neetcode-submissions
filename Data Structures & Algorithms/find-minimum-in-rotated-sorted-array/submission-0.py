class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0

        if nums[l] < nums[r]:
            return nums[l]

        min_nums = nums[l]

        while True:
            if nums[r] < min_nums:
                l = r
                r = r - 1
                min_nums = nums[l]
            else:
                return min_nums
