# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return root
#         def pre(root):
#             if root is None:
#                 return
#             if root.right is None and root.left is None:
#                 return
#             left = root.left
#             right = root.right
#             if left is not None:
#                 root.left = TreeNode(-1)
#                 root.left.left = left
#                 pre(root.left)
#             if right is not None:
#                 root.right = TreeNode(-1)
#                 root.right.right =right
#                 pre(root.right)
#         pre(root)
#         return root
    
# class Solution:
#     def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return root
#         def dfs(node):
#             if node is None:
#                 return
#             if node.left is None and node.right is None:
#                 return
#             left, right = node.left, node.right
#             if left is not None:
#                 node.left = TreeNode(-1)
#                 node.left.left = left
#                 dfs(left)
#             if right is not None:
#                 node.right = TreeNode(-1)
#                 node.right.right = right
#                 dfs(right)
#         dfs(root)
#         return root
# 操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈
# 操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈操你妈
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left is not None:
            root.left = TreeNode(-1,left = self.expandBinaryTree(root.left))
        if root.right is not None:
            root.right = TreeNode(-1,right = self.expandBinaryTree(root.right))
        return root