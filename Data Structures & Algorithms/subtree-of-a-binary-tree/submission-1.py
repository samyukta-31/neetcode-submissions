# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(r, s):
            if not r and not s:
                return True
            elif not r or not s:
                return False
            else:
                if r.val == s.val:
                    return sameTree(r.left, s.left) and sameTree(r.right, s.right)
                else:
                    return False

        def search(root):
            if not root:
                return False
            if sameTree(root, subRoot):
                return True
            else:
                return search(root.left) or search(root.right)

        return search(root)