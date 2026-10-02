class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(permutation, used):
            if len(permutation) == len(nums):
                self.res.append(permutation.copy())
                return
            for i, num in enumerate(nums):
                if num in used:
                    continue
                else:
                    used.append(num)
                    permutation.append(num)

                    dfs(permutation, used)

                    used.pop()
                    permutation.pop()
                
        dfs([], [])
        return self.res

            