# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recFinder(root, traversal):
            if not root:return traversal
            if(root):
                traversal.append(root.val)
                newt = recFinder(root.left, traversal)
                n2t = recFinder(root.right, newt)
                return n2t
            
        return recFinder(root, [])