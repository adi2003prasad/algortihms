# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
   
    def recFinder(self, root):
        if not root:return 100001
        if(root.left==root.right==None):return 1
        else:
            countLeft = 1
            countLeft+=self.recFinder(root.left)
            countRight = 1
            countRight+=self.recFinder(root.right)
            return min(countLeft, countRight)

    def minDepth(self, root: Optional[TreeNode]) -> int: # here the optional means a treenode of treenode like a nested loop
        z = self.recFinder(root)
        if(z>100000):return 0
        else:return z
