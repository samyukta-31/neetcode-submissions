class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elem = {num:0 for num in nums}
        for num in nums:
            elem[num] += 1
        for num, val in elem.items():
            if val > 1:
                return True
        return False