# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.value = root.val
        def dfs(node):
            if not node:
                return 1
            dfs(node.left) if node.left else 0
            self.count += 1
            if self.count == k:
                self.value = node.val
            dfs(node.right) if node.right else 0
            
            # return self.count
        dfs(root)
        return self.value