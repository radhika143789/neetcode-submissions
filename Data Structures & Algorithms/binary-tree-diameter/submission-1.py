# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # options are to take the sum of depth of left and right subtrees
        # or the depth from the root + the greater depth of the left or right subtree
        if not root:
            return 0
        
        lHeight, rHeight = self.getHeight(root.left), self.getHeight(root.right)
        diameter = lHeight + rHeight
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(diameter, sub)

    def getHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

