# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=False
    def dfs(self,root,sum,targetSum):
        if root is None or self.ans:
            return
        sum+=root.val
        if root.left is None and root.right is None:
            if sum==targetSum:
                self.ans=True
                return
        self.dfs(root.left,sum,targetSum)
        self.dfs(root.right,sum,targetSum)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.dfs(root,0,targetSum)
        return self.ans
