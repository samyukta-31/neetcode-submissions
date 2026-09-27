# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        path_max = root.val
        def dfs(node, path_max):
            if not node:
                return None
            if node.val >= path_max:
                self.good_nodes += 1
            
            new_max = max(node.val, path_max)
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        dfs(root, path_max)
        return self.good_nodes
