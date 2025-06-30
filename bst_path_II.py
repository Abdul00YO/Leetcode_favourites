# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out=[]
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root,sums,path):
            if root is None:
                return
            sums+=root.val
            path.append(root.val)
            if root.left is None and root.right is None:
                if sums==targetSum and sum(path)==targetSum:
                    self.out.append(path.copy())
            dfs(root.left,sums,path)
            dfs(root.right,sums,path)
            path.pop()
        dfs(root,0,[])
        return self.out
        
