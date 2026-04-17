# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # DFS
        # if not root: return None
        # root.right, root.left = root.left, root.right

        # self.invertTree(root.right)
        # self.invertTree(root.left)
        # return root

        # BFS
        # if not root: return None
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        # return root

        # Interative DFS
        if not root: return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right  = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root