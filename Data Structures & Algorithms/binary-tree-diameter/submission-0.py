# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      # Step 1: Initialize a variable to hold the max diameter found
        self.max_diameter = 0
        
        # Step 2: Define the recursive DFS function
        def dfs(curr):
            # Base case: an empty tree has a height of 0
            if not curr:
                return 0
            
            # Recursively find the height of the left and right subtrees
            left_height = dfs(curr.left)
            right_height = dfs(curr.right)
            
            # Update the max diameter if the path through the current node is larger
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of the current node to its parent
            # The height is 1 (for the current node) plus the tallest subtree
            return 1 + max(left_height, right_height)
        
        # Step 3: Call the function starting at the root
        dfs(root)
        
        # Step 4: Return the global maximum we found
        return self.max_diameter
        