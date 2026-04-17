# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []

        def dfs(node):
            if not node: return 

            # root → left → right
            res.append(node.val) # root
            dfs(node.left) # left
            dfs(node.right) # right

        
        dfs(root)
        return res