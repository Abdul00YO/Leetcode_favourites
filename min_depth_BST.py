# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list1=[]
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.count=0
        def dfs(root,count):
            if root==None:
                return
            count+=1
            if root.left==None and root.right==None:
                self.list1.append(count)
            dfs(root.left,count)
            dfs(root.right,count)
        dfs(root,self.count)
        return min(self.list1) if self.list1 else 0
