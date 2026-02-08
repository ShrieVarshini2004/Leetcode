class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def height(node):
            # Base case: empty subtree has height 0
            if node is None:
                return 0

            # Get height of left subtree
            left_height = height(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced

            # Get height of right subtree
            right_height = height(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced

            # If current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1

            # Return height if balanced
            return 1 + max(left_height, right_height)

        # Tree is balanced if height(root) != -1
        return height(root) != -1