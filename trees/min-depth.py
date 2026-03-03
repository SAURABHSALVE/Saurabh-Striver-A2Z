class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Base case: empty tree
        if root is None:
            return 0

        # If leaf node
        if root.left is None and root.right is None:
            return 1

        # If left child is None, go right
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # If right child is None, go left
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # If both children exist
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        return 1 + min(left_depth, right_depth)
s = Solution()
# Example usage:
# Constructing a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(s.minDepth(root))  # Output: 2
