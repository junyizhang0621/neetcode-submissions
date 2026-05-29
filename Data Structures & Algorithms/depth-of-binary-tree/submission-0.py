# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        resultMax = 0

        curr = self.dfs(root, 0)

        return curr


    def dfs(self, root, count):

        if root == None:
            return count

        count += 1

        left_max = self.dfs(root.left, count)
        right_max = self.dfs(root.right, count)

        return max(left_max, right_max)
        

        


        