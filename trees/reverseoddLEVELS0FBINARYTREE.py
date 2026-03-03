class Solution(object):
    def reverseOddLevels(self, root):

        if not root:
            return None

        def dfs(left_node, right_node, level):

            if not left_node or not right_node:
                return

            # If level is odd, swap values
            if level % 2 == 1:
                temp = left_node.val
                left_node.val = right_node.val
                right_node.val = temp

            # Go deeper symmetrically
            dfs(left_node.left, right_node.right, level + 1)
            dfs(left_node.right, right_node.left, level + 1)

        dfs(root.left, root.right, 1)

        return root
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
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
s.reverseOddLevels(root)
# Function to print tree in level order for verification
def print_level_order(node):

    if not node:
        return

    queue = [node]
    while queue:
        current = queue.pop(0)
        print(current.val, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
print_level_order(root)  # Output should reflect reversed odd levels

