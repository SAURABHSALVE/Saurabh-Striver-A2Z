# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        if root is None:
            return []
        
        arr = []
        arr.append(root.val)
        left_values = self.inorderTraversal(root.left)
        right_values = self.inorderTraversal(root.right)
        arr = left_values + arr  + right_values

        return arr
s = Solution()
# Example usage:
# Constructing a binary tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.inorderTraversal(root))  # Output: [1, 3, 2]


