# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, lb, rb):
            if not root:
                return True
            
            if not (lb <root.val < rb):
                return False
            
            else:
                return valid(root.left, lb, root.val) and valid(root.right, root.val, rb)
        
        return valid(root, float('-inf'), float('inf'))


    