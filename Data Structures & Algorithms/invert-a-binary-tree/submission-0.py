# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def preOrderTraversal(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            
            left = preOrderTraversal(node.left)
            right = preOrderTraversal(node.right)

        preOrderTraversal(root)

        return root
