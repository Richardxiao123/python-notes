# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        output=root
        if not root:
            return output
        if root.left or root.right:
            left=root.left
            root.left=root.right
            root.right=left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return output
