# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return None

            print(root.val)
            left = dfs(root.left)
            right = dfs(root.right)

            if p.val < root.val and q.val < root.val:
                return left
            elif p.val > root.val and q.val > root.val:
                return right
            else:
                return root
        return dfs(root)