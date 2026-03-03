class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        
        arr = []
        queue = [root]

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.pop(0)
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            arr.append(level_values)

        return arr

s = Solution()
# Example usage:
# Constructing a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(s.levelOrder(root))  # Output: [[1], [2, 3], [4, 5, 6, 7]]
