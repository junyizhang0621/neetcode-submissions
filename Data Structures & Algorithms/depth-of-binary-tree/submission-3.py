# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        return self.dfs(root, 0)

    def dfs(self,root, result):
        if not root:
            return result
        
        result += 1

        left = self.dfs(root.left, result)
        right = self.dfs(root.right, result)

        return max(left, right)




        