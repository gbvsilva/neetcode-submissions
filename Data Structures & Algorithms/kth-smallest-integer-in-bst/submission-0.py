# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def traverse(node):
            if node is None:
                return
            heapq.heappush(heap, node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        for _ in range(k-1):
            heapq.heappop(heap)
        return heap[0]