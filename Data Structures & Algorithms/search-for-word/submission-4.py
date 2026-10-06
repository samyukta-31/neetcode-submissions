class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i, j = 0, 0
        self.r1, self.r2, self.r3, self.r4 = False, False, False, False
        done = []
        def dfs(i, j, subword):
            if not word.startswith(subword):
                return False
            if subword == word:
                return True
            else:
                if i < len(board) - 1:
                    i += 1
                    if (i,j) not in done:
                        done.append((i,j))
                        self.r1 = dfs(i, j, subword + board[i][j])
                        done.pop()
                        if self.r1:
                            return self.r1
                    i -= 1
                if j < len(board[0]) - 1:
                    j += 1
                    if (i,j) not in done:
                        done.append((i,j))
                        self.r2 = dfs(i, j, subword + board[i][j])
                        done.pop()
                        if self.r2:
                            return self.r2
                    j -= 1
                if j > 0:
                    j -= 1
                    if (i,j) not in done:
                        done.append((i,j))
                        self.r3 = dfs(i, j, subword + board[i][j])
                        done.pop()
                        if self.r3:
                            return self.r3
                    j += 1
                if i > 0:
                    i -= 1
                    if (i,j) not in done:
                        done.append((i,j))
                        self.r4 = dfs(i, j, subword + board[i][j])
                        done.pop()
                        if self.r4:
                            return self.r4
                    i += 1
            return False

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                done.append((i,j))
                result = dfs(i, j, board[i][j])
                done.pop()
                if result:
                    return True
        return False
