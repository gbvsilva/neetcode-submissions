"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if not root:
            return
        node_map = {}
        def bfs(node):
            node_map[node] = Node(node.val)
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                for neighbor in curr.neighbors:
                    if neighbor not in node_map:
                        node_map[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    node_map[curr].neighbors.append(node_map[neighbor])
        bfs(root)
        return node_map[root]
