# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = f""
        def dfs(node, string):
            if not node:
                return string+ "|" + "*"
            string = string  + "|" + f"{node.val}"
            string = dfs(node.left, string)
            string = dfs(node.right, string)
            return string
        print(dfs(root, string))
        return dfs(root, string)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_l = data.split("|")
        tree = TreeNode()
        self.i = 0
        curr = tree
        def dfs(curr):
            self.i += 1
            val = data_l[self.i]
            if val == "*":
                return None
            else:
                curr = TreeNode(data_l[self.i])
            val = data_l[self.i]
            curr.left = dfs(curr.left)
            curr.right = dfs(curr.right)
            return curr
        
        return dfs(curr)

