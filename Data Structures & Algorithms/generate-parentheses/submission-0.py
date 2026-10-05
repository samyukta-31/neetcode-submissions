class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        types = ["(",")"]

        self.res = []
        res = []

        def dfs(res, i, unmatched, opened):
            if i == 2*n:
                if unmatched == 0:
                    self.res.append("".join(res.copy()))
                return
            for t in types:
                if t == "(":
                    unmatched += 1
                    opened += 1
                    if unmatched <= n:
                        res.append(t)
                        dfs(res, i + 1, unmatched, opened)
                        res.pop()
                    opened -= 1
                    unmatched -= 1
                elif t == ")":
                    if unmatched > 0:
                        unmatched -= 1
                        res.append(t)
                        dfs(res, i + 1, unmatched, opened)
                        res.pop()
                        unmatched += 1
        dfs(res, 0, 0, 0)
        return self.res
