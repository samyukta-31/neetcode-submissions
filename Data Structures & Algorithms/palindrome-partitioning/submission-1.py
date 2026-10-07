class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.palindromes = []

        def dfs(i, j, res):
            if i == len(s):
                self.palindromes.append(res.copy()) if res else None
                return
            if j == len(s) + 1:
                return
            subword = s[i:j]
            if subword == subword[::-1]:
                res.append(subword)
                old_j = j
                old_i = i
                i = old_j
                j = i + 1
                dfs(i, j, res)
                i = old_i
                j = old_j
                res.pop()

            j += 1
            dfs(i, j, res)
            j -= 1
        
        dfs(0, 1, [])
        return self.palindromes


                