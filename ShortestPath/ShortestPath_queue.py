from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # Number of nodes in the graph
        n = len(graph)

        # Calculate the final state where all nodes are visited
        final_state = (1 << n) - 1

        # Initialize a deque to use as a queue for BFS traversal
        queue = deque()

        # Use a set to keep track of visited nodes and their states
        visited = set()

        # Initialize the queue with starting states for each node
        for i in range(n):
            queue.append((i, 1 << i, 0))

        # Perform BFS traversal
        while queue:
            # Dequeue the front element to get the current node, state, and length
            node, state, length = queue.popleft()

            # Check if the current state is the final state (all nodes visited)
            if state == final_state:
                return length

            # Check if the current node and state have been visited before
            if (node, state) in visited:
                continue

            # Mark the current node and state as visited
            visited.add((node, state))

            # Explore neighbors of the current node
            for neighbor in graph[node]:
                # Update the state by setting the bit corresponding to the neighbor to 1
                new_state = state | (1 << neighbor)
                # Enqueue the neighbor, new state, and updated length for further exploration
                queue.append((neighbor, new_state, length + 1))

        # If the loop completes without finding a path that visits all nodes, return -1
        return -1
# Example usage:
sol = Solution()
graph1 = [[1,2,3],[0],[0],[0]]
print(sol.shortestPathLength(graph1))  # Output: 4

graph2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(sol.shortestPathLength(graph2))  # Output: 4
