class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        
        def dfs(i, sub):
            if i == len(nums):
                self.res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i + 1, sub)
            sub.pop()
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1
            dfs(next_i, sub)
            
                
        dfs(0, [])
        return self.res
