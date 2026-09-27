class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        self.subs = []
        i = 0
        def dfs(i, sub):
            if i < len(nums):
                sub.append(nums[i])
                dfs(i+1, sub)
                sub.pop()
                dfs(i+1, sub)
            else:
                sub_2 = sub.copy()
                self.subs.append(sub_2)

        dfs(i, sub)
        return self.subs
            