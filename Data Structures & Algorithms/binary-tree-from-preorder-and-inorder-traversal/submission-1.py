# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        inorder_index = {val: i for i, val in enumerate(inorder)}
        
        def dfs(start, end):
            if start >= end:
                return None
            node = TreeNode(preorder[self.i])
            k = inorder_index[preorder[self.i]]
            self.i += 1
            node.left = dfs(start, k)
            node.right = dfs(k+1, end)
            return node 
        return dfs(0, len(inorder))
                
        