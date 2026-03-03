## basic version 
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        
        arr = []
        
        # Step 1: Add root value
        arr.append(root.val)
        
        # Step 2: Traverse left subtree
        left_values = self.preorderTraversal(root.left)
        
        # Step 3: Traverse right subtree
        right_values = self.preorderTraversal(root.right)
        
        # Step 4: Combine results
        arr = arr + left_values + right_values
        
        return arr

s = Solution()
# Example usage:
# Constructing a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.preorderTraversal(root))  # Output: [1, 2, 3]
