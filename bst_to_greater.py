# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(root, sum):
            if not root: return sum
            
            if root.right: sum = traverse(root.right, sum)
                
            root.val += sum
            sum = root.val
            
            if root.left: sum = traverse(root.left, sum)
                
            return sum
        
        traverse(root, 0)
        
        return root
