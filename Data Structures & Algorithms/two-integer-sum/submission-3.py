class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_i = {num:i for i, num in enumerate(nums)}
        for i, num_1 in enumerate(nums):
            num_2 = target - num_1
            if num_2 in nums and num_i[num_2] != i:
                return [i, num_i[num_2]]





        