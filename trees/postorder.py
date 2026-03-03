# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if root is None:
            return []
        
        arr = []

        lefthalf = self.postorderTraversal(root.left)
        righthalf = self.postorderTraversal(root.right)
        arr.append(root.val)

        arr = lefthalf + righthalf + arr
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
print(s.postorderTraversal(root))  # Output: [3, 2, 1]
