class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for val in nums:
            if val in s:
                return val
            s.add(val)
