class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        _sum = 0
        self.res = []

        def dfs(_sum, i, res_sf):
            if i < len(nums):
                if _sum < target:
                    res_sf.append(nums[i])
                    dfs(_sum + nums[i], i, res_sf)
                    res_sf.pop()
                    dfs(_sum, i + 1, res_sf)
                elif _sum == target:
                    self.res.append(res_sf.copy())
                else:
                    return
        dfs(_sum, 0, [])
        return self.res

