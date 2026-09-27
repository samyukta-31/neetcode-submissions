class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {val: i for i, val in enumerate(nums)}
        for j in range(0,len(nums)):
            if target - nums[j] in h.keys() and h[target - nums[j]]!=j:
                return [j, h[target - nums[j]]]




        