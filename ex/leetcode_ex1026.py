# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode], max_num: int, min_num: int) -> None:
            if node == None:
                nonlocal ans
                ans = max(ans,max_num-min_num)
                return
            if node.val > max_num:
                max_num = node.val
            if node.val < min_num:
                min_num = node.val
            dfs(node.left,max_num,min_num)
            dfs(node.right,max_num,min_num)
        dfs(root,root.val,root.val)
        return ans