# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recFinder(root):
            if not root:return 0
            if(root):
                leftroot, rightroot = recFinder(root.left), recFinder(root.right)
                if(abs(leftroot-rightroot)>1):return -1
                if(leftroot<0) or (rightroot<0):return -1
                return max(leftroot, rightroot)+1
        return recFinder(root)>=0