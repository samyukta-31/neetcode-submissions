class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        def dfs(i, res, _sum):
            if _sum == target:
                self.res.append(res.copy())
            elif _sum < target:
                if i < len(candidates):
                    res.append(candidates[i])
                    dfs(i + 1, res, _sum + candidates[i])
                    res.pop()
                    i += 1
                    while i < len(candidates) and candidates[i] == candidates[i - 1]:
                        i += 1
                    dfs(i, res, _sum)
                else:
                    return
            else:
                return
        dfs(0, [], 0)
        return self.res
