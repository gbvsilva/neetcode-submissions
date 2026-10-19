# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, max_val):
            if node is None:
                return 0
            count = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return count + traverse(node.left, max_val) + traverse(node.right, max_val)

        return traverse(root, root.val)