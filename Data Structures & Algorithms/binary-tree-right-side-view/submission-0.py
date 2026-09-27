# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        rights = []
        level = 0
        def dfs(node, level):
            if not node:
                return None
            if len(rights) == level:
                rights.append(node.val)
            if node.right:
                dfs(node.right, level+1)
                dfs(node.left, level+1)
            elif node.left:
                dfs(node.left, level+1)

        dfs(root, level)
        return rights