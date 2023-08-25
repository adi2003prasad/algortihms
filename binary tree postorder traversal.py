# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tt = []
        
        def recFinder(root):
            if not root: return
            recFinder(root.left)
            recFinder(root.right)
            tt.append(root.val)

        recFinder(root)
        return tt 