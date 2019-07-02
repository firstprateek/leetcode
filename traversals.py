def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right

 def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45785/Share-my-two-Python-iterative-solutions-post-order-and-modified-preorder-then-reverse


def countArrangement(self, N):
    def count(i, X):
        if i == 1:
            return 1
        return sum(count(i - 1, X - {x})
                   for x in X
                   if x % i == 0 or i % x == 0)
    return count(N, set(range(1, N + 1)))