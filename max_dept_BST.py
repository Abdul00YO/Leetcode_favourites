# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list1=[]
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.count=0
        def check(root,count):
            if root==None:
                return
            count+=1
            check(root.left,count)
            self.list1.append(count)
            check(root.right,count)
            self.list1.append(count)
        check(root,self.count)
        return max(self.list1) if self.list1 else 0
