# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            leftBalanced, leftHeight = dfs(node.left)
            rightBalanced, rightHeight = dfs(node.right)

            balanced = (
                leftBalanced and
                rightBalanced and
                abs(leftHeight - rightHeight) <= 1
            )

            height = 1 + max(leftHeight, rightHeight)

            return [balanced, height]

        return dfs(root)[0]