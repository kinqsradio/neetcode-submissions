"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root

        # # BFS
        # q = deque([root])
        # while q:
        #     levelSize = len(q)
        #     while levelSize:
        #         node = q.popleft()
        #         if levelSize > 1:
        #             node.next = q[0]
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #         levelSize -= 1
        # return root

        # DFS
        mp = {}
        def dfs(node, depth):
            if not node: return
            
            if depth not in mp:
                mp[depth]=node
            else:
                mp[depth].next = node
                mp[depth] = node
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return root