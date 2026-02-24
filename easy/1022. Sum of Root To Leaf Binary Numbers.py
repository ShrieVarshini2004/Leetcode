class Solution:
    def sumRootToLeaf(self, root):
        self.result = 0

        def dfs(node, current):
            if not node:
                return

            # Shift left and add node value
            current = (current << 1) | node.val

            # If leaf node, add to result
            if not node.left and not node.right:
                self.result += current
                return

            # Recurse left and right
            dfs(node.left, current)
            dfs(node.right, current)

        dfs(root, 0)
        return self.result