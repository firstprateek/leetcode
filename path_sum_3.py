# Somehow this does not read left_paths for some reason
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        count = 0
        if not root:
            return count 
        
        left_paths = []
        right_paths = []
        def num_of_paths(root):
            nonlocal left_paths
            nonlocal right_paths
            nonlocal count
            
            left_paths.clear()
            right_paths.clear()
            
            if root.left:
                left_paths = [ path + root.val for path in num_of_paths(root.left)]
            
            if root.right:
                right_paths = [ path + root.val for path in num_of_paths(root.right)]
            
            all_paths = left_paths + right_paths + [root.val]
            print("node.val: {0}, all_paths: {1}".format(root.val, all_paths))
            print("root.left: {0}, left_paths: {1}".format(root.left, left_paths))
            print("root.right: {0}, right_paths: {1}".format(root.right, right_paths))
            count += all_paths.count(sum)
            
            return all_paths
        
        num_of_paths(root)
        
        return count

# This worked

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        count = 0
        if not root:
            return count 
        
        def num_of_paths(root):
            nonlocal count
            
            left_paths = []
            right_paths = []
            
            if root.left:
                left_paths = [ path + root.val for path in num_of_paths(root.left)]
            
            if root.right:
                right_paths = [ path + root.val for path in num_of_paths(root.right)]
            
            all_paths = left_paths + right_paths + [root.val]
            count += all_paths.count(sum)
            
            return all_paths
        
        num_of_paths(root)
        
        return count
